from itertools import product
from math import prod
import motor.motor_asyncio
from bson.objectid import ObjectId


# connection string gotten by Mongo Atlas
connection_string = \
    "mongodb+srv://renatamoon:264500@clusterlearning.b6jyp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

# passing it to a variable
client = motor.motor_asyncio.AsyncIOMotorClient(connection_string)

# getting the database from MongoAtlas
database = client.new_database

# getting the collection from MongoAtlas
products_collection = database.get_collection("products")


# ---- Helpers

def product_helpers(product) -> dict:
    return {
        "product_id": int(product["_id"]),
        "productTitle": str(product["productTitle"]),
        "productPrice": float(product["productPrice"]),
        "productDescription": str(product["productDescription"]),
    }


# CRUD OPERATIONS

# GET all the products from the database
async def get_all_products():
    products = []
    async for product in products_collection.find():
        products.append(product_helpers(product))
    return {"allProducts": products}


# POST a new product in the database
async def post_product(product: dict) -> dict:
    product = await products_collection.insert_one(product)
    new_product = await products_collection.find_one({"_id": product.inserted_id})
    return product_helpers(new_product)


# GET a product by an ID
async def get_product_by_id(product_id: str) -> dict:
    product = await products_collection.find_one({"_id": ObjectId(product_id)})
    if product:
        return product_helpers(product)


# UPDATE a product by ID
async def update_product(product_id: str, data: dict):
    if len(data) < 1:
        return False
    
    product = await products_collection.find_one({"_id": ObjectId(product_id)})
    if product:
        updated_product = await products_collection.update_one(
            {"_id": ObjectId(product_id)}, {"$set": data}
        )
        if update_product:
            return True
        return False


# DELETE PRODUCT
async def delete_product(product_id: str):
    product = await products_collection.find_one({"_id": ObjectId(product_id)})
    if product:
        await products_collection.delete_one({"_id": ObjectId(product_id)})
        return True
        
