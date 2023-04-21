

from pydantic import BaseModel


class RoleCreate(BaseModel):
    roleName:str
    roleDesc:str

    