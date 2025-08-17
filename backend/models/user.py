from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    
class User(BaseModel):
    id: Optional[int] 
    name: str
    email: EmailStr
