from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text


class Products(Base):
    __tablename__ = "product"
    id = Column(Integer,primary_key=True,nullable=False)
    name = Column(String,nullable=False)
    category = Column(String,nullable=False)
    description = Column(String)
    image = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    

class User(Base):
    __tablename__ = "user"
    id = Column(Integer,primary_key=True,nullable=False)
    name = Column(String,nullable=False)
    # email = Column(String, nullable = False)
    # mobile_num = Column(String, nullable=False)
    password = Column(String);