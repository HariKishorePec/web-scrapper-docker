from sqlalchemy import Column, Integer, String, Float, Date
from database import Base


class BulkDeals(Base):
    __tablename__ = "bulk_deals"

    id = Column(Integer, primary_key=True, index=True)
    security_code = Column(Integer)
    security_name = Column(String)
    client_name = Column(String)
    deal_type = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    deal_date = Column(Date)
