from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient


from pymongo import MongoClient

# connection string gotten by Mongo Atlas
connection_string = \
    "mongodb+srv://renatamoon:264500@clusterlearning.b6jyp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

# passing it to a variable
client = MongoClient(connection_string)

# getting the database from MongoAtlas
database = client['new_database']

# getting the collection from MongoAtlas
collection = database['products']


# ---- Models

# Model of the class Product
class ProductSchema(BaseModel):
    id: int
    productTitle: str
    productPrice: float
    productDescription: str

    class Config:
        extra : "forbid"


# ---- Helpers

def product_helpers(product) -> dict:
    return {
        "id": int(product["_id"]),
        "productTitle": str(product["productTitle"]),
        "productPrice": float(product["productPrice"]),
        "productDescription": str(product["productDescription"]),
    }


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
async def get_an_products_by_id():
    pass


# POST A PRODUCT - endpoint to create a new product on out database
@app.post("/post-product", tags=["Product Registry"])
async def add_product():
    pass