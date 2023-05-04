from fastapi import FastAPI, Depends
import model
from database import engine

from routes import user_route

app = FastAPI(title="CosMark APIs")


model.Base.metadata.create_all(engine)


app.include_router(user_route.router)

@app.get('/')
async def home():
    return "Welcome to CoskMark APIs, use authorised API Key to access all the APIs. Thank you!"