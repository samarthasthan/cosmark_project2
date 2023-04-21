from fastapi import FastAPI, Depends
import model
from database import engine
from routes.admin import admin_route
from routes.user import user_auth

app = FastAPI(title="CosMark APIs")


model.Base.metadata.create_all(engine)

app.include_router(admin_route.router)
app.include_router(user_auth.router)

@app.get('/')
async def home():
    return "Welcome to CoskMark APIs, use authorised API Key to access all the APIs. Thank you!"