from fastapi import FastAPI


app = FastAPI()


products = []


# endpoints
@app.get('/', tags=["MainPage"])
async def Index():
    return {"Message": "The FASTAPI is now working"}


# endpoint to get all the articles
@app.get("/products", tags=["Products"])
async def get_all_products():
    return {"allProducts": products}


# endpoint to get a single article
@app.get("/get-product{id}", tags=["Products"])
async def get_an_products_by_id(id: int):
    return {"searchedProduct": {id}}


