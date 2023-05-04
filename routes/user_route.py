from typing import List
import fastapi
from fastapi import APIRouter, Depends
from database import SessionLocal,get_db
from schemas import user_schema
import model 

router=APIRouter(prefix='/user',tags=['User'])

@router.post("/signup")
async def sign_up(details:user_schema.SignUp,db:SessionLocal=Depends(get_db)):
    new_user=model.Users(**details.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/signup/activist")
async def become_activist(details:user_schema.Activist,db:SessionLocal=Depends(get_db)):
    new_activist=model.Activists(**details.dict())
    db.add(new_activist)
    db.commit()
    db.refresh(new_activist)
    return new_activist

@router.get("",response_model=List[user_schema.GetUser])
async def get_users(db:SessionLocal=Depends(get_db)):
    users=db.query(model.Users).all()
    return users


@router.get("/activist/{id}")
async def get_activist_by_id(id:int,db:SessionLocal=Depends(get_db)):
    activist=db.query(model.Activists).filter(model.Activists.user_id==id).first()
    return activist