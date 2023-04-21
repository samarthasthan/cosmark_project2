import fastapi
from fastapi import APIRouter, Depends
from database import SessionLocal,get_db
from schemas.user import user_auth_schema
import model 

router=APIRouter(prefix='/user',tags=['User'])

@router.post("/signup")
async def sign_up(details:user_auth_schema.SignUp,db:SessionLocal=Depends(get_db)):
    new_user=model.User(**details.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user