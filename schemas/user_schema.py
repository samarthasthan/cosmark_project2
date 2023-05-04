from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from model import Role

class SignUp (BaseModel):
    user_name:str
    pincode:int
    user_image:str
    last_active:datetime
    role:Role
    class Config:
        orm_mode = True


class Activist(BaseModel):
    user_id:int
    expertise_in:str

    class Config:
        orm_mode = True

class GetUser(BaseModel):
    user_name:str
    pincode:int
    user_image:str
    last_active:datetime
    role:Role
    
    class Config:
        orm_mode = True