import motor.motor_asyncio


# connection string gotten by Mongo Atlas
CONNECTION_STRING = \
    "mongodb+srv://renatamoon:264500@clusterlearning.b6jyp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

# passing it to a variable
client = motor.motor_asyncio.AsyncIOMotorClient(CONNECTION_STRING)

# getting the database from MongoAtlas
database = client.new_database

# getting the collection from MongoAtlas
collection = database.get_collection("products")


# ---- Helpers

def product_helpers(product) -> dict:
    return {
        "id": int(product["_id"]),
        "productTitle": str(product["productTitle"]),
        "productPrice": float(product["productPrice"]),
        "productDescription": str(product["productDescription"]),
    }