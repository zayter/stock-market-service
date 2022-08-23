
import requests
from requests.exceptions import HTTPError
import os

from . import (
    StockMapper,
)

from stock.exceptions import (
    StockServiceNotFoundFailure,
    StockServiceBadRequestFailure
)


class StockService:
    api_key = os.environ['API_KEY']
    base_url = 'https://www.alphavantage.co'
    function = 'TIME_SERIES_DAILY'

    def __init__(self, symbol, params):
        self.symbol = symbol
        self.outputsize = params.get('outputsize')

    def retrieve(self):
        try:
            url = f'{self.base_url}/query'
            response = requests.get(url, params=self.__payload())
            response.raise_for_status()
            data = response.json()
            if (data.get('Error Message') is None):
                return StockMapper(self.symbol, data).parse_to_stock()
            else:
                raise StockServiceNotFoundFailure(
                        detail=data.get('Error Message')
                    )

        except HTTPError as http_err:
            raise StockServiceBadRequestFailure(code=http_err.code)

    def __payload(self):
        return {
            'function': self.function,
            'symbol': self.symbol,
            'outputsize': self.outputsize or 'compact',
            'apikey': self.api_key
        }
