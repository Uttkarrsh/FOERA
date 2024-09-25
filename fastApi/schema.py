from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from typing import List

class UserCreate(BaseModel):
    name: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    name: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    user_id: int
    user_name: str


class ProductCreate(BaseModel):
    name: str
    category: str
    description: str
    image: str
    cost:float

class ProductResponse(BaseModel):
    id:int
    name:str
    category:str
    image:str
    created_at: datetime
    cost:float

    class Config:
        from_attributes = True

class WishlistItemResponse(BaseModel):
    user_id: int
    product: ProductResponse

    class Config:
        from_attributes = True

class CartItemCreate(BaseModel):
    quantity: float

class CartItemResponse(BaseModel):
    id: int
    quantity: float
    user_id: int
    product: ProductResponse
    created_at: datetime

    class Config:
        from_attributes = True

class CheckoutResponse(BaseModel):
    cart_items: List[CartItemResponse]
    total_cost: float

class AddressCreate(BaseModel):
    name: Optional[str]
    address_line1: str
    address_line2: str
    city: str
    state: str
    pincode: str

class AddressResponse(BaseModel):
    id: int
    name: Optional[str]
    address_line1: str
    address_line2: str
    city: str
    state: str
    pincode: str
    user_id: int

    class Config:
        from_attributes = True
    
class OrderResponse(BaseModel):
    message: str
    order_id: int
    total_cost: float
    cart_items: List[CartItemResponse]

    class Config:
        from_attributes = True

class CheckoutResponse(BaseModel):
    order_id: int
    cart_items: List[CartItemResponse]
    total_cost: float

    class Config:
        from_attributes = True