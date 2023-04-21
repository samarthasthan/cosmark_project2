
import fastapi
from fastapi import APIRouter, Depends
import model
from schemas.admin import admin_schema
from database import SessionLocal, get_db

router=APIRouter(prefix='/admin',tags=['Admin'])


@router.post("/role")
async def create_role(role:admin_schema.RoleCreate,db:SessionLocal=Depends(get_db)):
  
    new_role= model.Role(**role.dict())
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role