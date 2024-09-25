from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime




class Products(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    description = Column(String)
    image = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    cost = Column(Float, nullable=False)  
    wishlist_items = relationship("Wishlist", back_populates="product")
    cart_items = relationship("Cart", back_populates="product")


    

class User(Base):
    __tablename__ = "user"
    id = Column(Integer,primary_key=True,nullable=False)
    name = Column(String,nullable=False)
    # email = Column(String, nullable = False)
    # mobile_num = Column(String, nullable=False)
    password = Column(String);
    wishlist_items = relationship("Wishlist", back_populates="user")
    cart_items = relationship("Cart", back_populates="user")
    address = relationship("Address", back_populates="user")


class Wishlist(Base):
    __tablename__ = "wishlist"
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    user = relationship("User", back_populates="wishlist_items")
    product = relationship("Products", back_populates="wishlist_items")

class Cart(Base):
    __tablename__ = "cart"
    id = Column(Integer, primary_key=True, nullable=False)
    quantity = Column(Float, nullable=False)  
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    user = relationship("User", back_populates="cart_items")
    product = relationship("Products", back_populates="cart_items")
    
class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=True)
    address_line1 = Column(String, nullable=False)
    address_line2 = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    pincode = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship("User", back_populates="address")

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    total_cost = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class OrderItem(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
    quantity = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)
