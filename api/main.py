from fastapi import FastAPI
from .domain.models import Product
from .infraestructure.mongo import database, collection, product_helpers
from bson.objectid import ObjectId


app = FastAPI()


# endpoints
@app.get('/', tags=["MainPage"])
async def Index():
    return {"Message": "The FASTAPI is now working"}


# GET ALL PRODUCTS - endpoint to get all the articles
@app.get("/products", tags=["Products"])
async def retrieve_all_products():
    products = []
    async for product in collection.find():
        products.append(product_helpers(product))
    return {"allProducts": products}


# GET A PRODUCT BY ID - endpoint to get a single article
@app.get("/get-product{id}", tags=["Products"])
async def get_an_products_by_id(id: int):
    return {"searchedProduct": {id}}


# POST A PRODUCT - endpoint to create a new product on out database
@app.post("/post-product", tags=["Product Registry"])
async def add_product(product: Product):
    return {"MESSAGE": "THE PRODUCT WAS ADDED WITH SUCCESS"}