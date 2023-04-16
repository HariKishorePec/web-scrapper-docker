from pydantic import BaseModel
from typing import Optional
from datetime import date


class BulkDealsBase(BaseModel):
    security_code: int
    security_name: str
    client_name: str
    deal_type: str
    quantity: int
    price: float
    deal_date: date


class BulkDealsCreate(BulkDealsBase):
    pass


class BulkDealsDelete(BaseModel):
    pass


class BulkDealsUpdate(BulkDealsBase):
    pass


class BulkDeals(BulkDealsBase):
    id: int

    class Config:
        orm_mode = True
