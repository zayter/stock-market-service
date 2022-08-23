"""
URL mappings for the stock app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter
from stock.views import StockViewSet

router = DefaultRouter()
router.register(r'stocks', StockViewSet, basename='stock')
app_name = 'stock'

urlpatterns = [
    path('', include(router.urls)),
]
