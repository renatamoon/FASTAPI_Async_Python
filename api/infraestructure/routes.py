from hashlib import new
from math import prod
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from infraestructure.mongo import (                                     
                                    get_all_products, 
                                    get_product_by_id, 
                                    post_product, 
                                    update_product, 
                                    delete_product)
from infraestructure.models import (
    ErrorResponseModel,
    ResponseModel,
    ProductSchema,
    UpdateProductSchema    
)


router = APIRouter()



# CREATE PRODUCT
@router.post("/", response_description="Product information added into the database")
async def add_product_information(product: ProductSchema = Body(...)):
    product = jsonable_encoder(product)
    new_product = await post_product(product)
    return ResponseModel(new_product, "PRODUCT ADDED WITH SUCCESS")


# GET ALL THE PRODUCTS
@router.get("/", response_description="Products Retrieved")
async def get_