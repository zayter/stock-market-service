"""
Tests for Stock APIs.
"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import (
    StockRequest,
)
from stock.tests.helpers import vcr

STOCK_URL = reverse('stock:stock-list')


def detail_url(stock_id):
    """Create and return a stock detail URL."""
    return reverse('stock:stock-detail', args=[stock_id])


def create_user(**params):
    """Create and return a new user."""
    return get_user_model().objects.create_user(**params)


class PublicStockAPITests(TestCase):
    """Test unauthenticated API requests."""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required to call API."""
        res = self.client.get(detail_url('AMZN'))

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateStockApiTests(TestCase):
    """Test authenticated API requests."""

    def setUp(self):
        self.client = APIClient()
        self.user = create_user(email='user@example.com', password='test123')
        self.client.force_authenticate(self.user)
        self.ticker = 'AMZN'

    @vcr.use_cassette()
    def test_get_stock_detail(self):
        """Test get stock detail."""
        url = detail_url(self.ticker)
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn('symbol', res.data)
        self.assertIn('previous', res.data)
        self.assertIn('close_deviation', res.data)
        current_cost = float(res.data['close'])
        previous_cost = float(res.data['previous']['close'])
        calculated_cost_deviation = round(current_cost - previous_cost, 4)
        response_cost_deviation = round(float(res.data['close_deviation']), 4)
        self.assertEqual(response_cost_deviation, calculated_cost_deviation)

    @vcr.use_cassette()
    def test_create_log_record(self):
        url = detail_url(self.ticker)
        self.client.get(url)

        another_user = create_user(
            email='user2@example.com',
            password='test123'
        )
        self.client.force_authenticate(another_user)
        self.client.get(url)

        sr = StockRequest.objects.filter(user=self.user)
        self.assertEqual(sr.count(), 1)

        sr = StockRequest.objects.all()
        self.assertEqual(sr.count(), 2)

    @vcr.use_cassette()
    def test_invalid_stock(self):
        url = detail_url('NOTAMZN')
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_list_of_request(self):
        url = STOCK_URL
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
