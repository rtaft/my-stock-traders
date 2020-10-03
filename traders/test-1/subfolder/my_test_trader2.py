from traders.interface import TraderInterface, TraderSchema
from marshmallow import Schema, fields, validate, EXCLUDE

from helper import MyTraderSchema2

class MyTraderBuyer2(TraderInterface):
    def setup(self, params):
        super(MyTraderBuyer, self).setup(params)
        valid_data = MyTraderSchema2(unknown=EXCLUDE).load(params)
        self.symbol = valid_data.get('symbol')

    def get_schema(self):
        return MyTraderSchema2()

    def get_name(self):
        return 'My Trader 2'

    def process_day(self, current_date, datasets, simulation_trade_id):
        apple = datasets.get(self.symbol)
        if apple:
            current_price = apple.get_current_price()
            if current_price and (self.portfolio.cash) > current_price.trade_close:
                quantity = (self.portfolio.cash) // current_price.trade_close
                self.buy(self.symbol, quantity, simulation_trade_id)
