from fastapi import FastAPI
from api.infraestructure.models import ProductSchema
from infraestructure.routes import router
from fastapi import APIRouter, Body


app = FastAPI()

app.include_router(router, tags=["Product"], prefix="/product")


# HOME endpoint
@app.get('/', tags=["MainPage"])
async def Index():
    return {"Message": "The FASTAPI is now working"}
