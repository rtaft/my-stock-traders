from traders.interface import TraderInterface, TraderSchema

class MyTraderSchema2(TraderSchema):
    symbol = fields.String(required=True, metadata=dict(notes="Symbol of the stock to buy."))
