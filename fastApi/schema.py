from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    name: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class ProductCreate(BaseModel):
    name: str
    category: str
    description: str
    image: str

class ProductResponse(BaseModel):
    id:int
    name:str
    category:str
    image:str
    created_at: datetime

    class Config:
        orm_mode = True