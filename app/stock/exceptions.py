from rest_framework.exceptions import APIException


class StockServiceNotFoundFailure(APIException):
    status_code = 404
    default_detail = 'Service temporarily unavailable, try again later.'


class StockServiceBadRequestFailure(Exception):
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'
