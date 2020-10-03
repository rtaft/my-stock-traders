from traders.interface import TraderInterface, TraderSchema
from marshmallow import Schema, fields, validate, EXCLUDE

class MyTraderSchema2(TraderSchema):
    symbol = fields.String(required=True, metadata=dict(notes="Symbol of the stock to buy."))
