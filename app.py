import sys
import asyncio
from fastapi import FastAPI
sys.path = ['', '..'] + sys.path[1:]
from router import router

app = FastAPI()

@app.get('/')
async def Home():
    return "welcome home"

app.include_router(router)

