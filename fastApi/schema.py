from pydantic import BaseModel, EmailStr

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