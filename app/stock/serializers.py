"""
Serializers for Stock APIs
"""
from rest_framework import serializers


class StockSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    symbol = serializers.CharField(max_length=256)
    date = serializers.CharField(max_length=256)
    open = serializers.DecimalField(max_digits=None, decimal_places=4)
    high = serializers.DecimalField(max_digits=None, decimal_places=4)
    low = serializers.DecimalField(max_digits=None, decimal_places=4)
    close = serializers.DecimalField(max_digits=None, decimal_places=4)
    volume = serializers.IntegerField()
    previous = serializers.JSONField()
    close_deviation = serializers.DecimalField(
        max_digits=None,
        decimal_places=4
    )


class StockRequestSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    symbol = serializers.CharField(max_length=256)
    requested_at = serializers.CharField(max_length=256)
