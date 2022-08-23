"""
Views for the stock APIs
"""
from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiTypes,
)

from rest_framework import (
    viewsets,
)
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from core.models import (
    StockRequest,
)

from stock import (
    serializers,
)

from stock.services import StockService


@extend_schema_view(
    retrieve=extend_schema(
        parameters=[
            OpenApiParameter(
                'outputsize',
                OpenApiTypes.STR,
                description='compact or full',
            ),
        ]
    )
)
class StockViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.StockSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        sr = StockRequest.objects.filter(user=self.request.user)
        serializer = serializers.StockRequestSerializer(
            instance=sr, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        StockRequest.objects.create(user=self.request.user, symbol=pk)
        stock = StockService(pk, self.request.query_params).retrieve()
        serializer = serializers.StockSerializer(instance=stock)
        return Response(serializer.data)
