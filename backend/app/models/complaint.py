from sqlalchemy import Column, Integer, String

from app.database.base import Base


class Complaint(Base):
    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String)
    product_name = Column(String)
    batch_number = Column(String)
    risk_level = Column(String)