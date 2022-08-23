class Stock(object):
    def __init__(self, **kwargs):
        for field in (
            'symbol',
            'date',
            'open',
            'high',
            'low',
            'close',
            'volume',
            'previous',
            'close_deviation'
        ):
            setattr(self, field, kwargs.get(field, None))


class StockMapper(object):
    def __init__(self, symbol, data):
        self.symbol = symbol
        stock_info_per_day = data['Time Series (Daily)']
        self.last_stock = list(stock_info_per_day.items())[0]
        self.previous_stock = list(stock_info_per_day.items())[1]

    def parse_to_stock(self):
        return Stock(
            symbol=self.symbol,
            date=self.last_stock[0],
            open=self.__open(),
            high=self.__high(),
            low=self.__low(),
            close=self.__close(),
            volume=self.__volume(),
            previous=self.__previous,
            close_deviation=self.__close_deviation()
        )

    def __open(self):
        return self.last_stock[1]['1. open']

    def __high(self):
        return self.last_stock[1]['2. high']

    def __low(self):
        return self.last_stock[1]['3. low']

    def __close(self):
        return float(self.last_stock[1]['4. close'])

    def __volume(self):
        return self.last_stock[1]['5. volume']

    def __previous(self):
        return {
            'date': self.previous_stock[0],
            'close': self.previous_stock[1]['4. close'],
        }

    def __close_deviation(self):
        return self.__close() - float(self.__previous()['close'])
