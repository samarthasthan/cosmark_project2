from datetime import datetime
from pydantic import BaseModel


class SignUp (BaseModel):
    userName:str
    pincode:int
    userImage:str
    lastActive:datetime
    role:int