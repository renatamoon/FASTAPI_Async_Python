from pydantic import BaseModel
from typing import Optional


# ---- Models

# Model of the class Product
class ProductSchema(BaseModel):
    product_id: int
    productTitle: str
    productPrice: float
    productDescription: str
    

    class Config:
        schema_extra = {
            "product": {
                "product_id": "123456",
                "productTitle": "Milk for Vegans",
                "productPrice": 123.45,
                "productDescription": "This milk is made by nuts and it's one of the best for vegans"
            }
        }


# Update product Schema
class UpdateProductSchema(BaseModel):
    product_id: Optional[int]
    productTitle: Optional[str]
    productPrice: Optional[float]
    productDescription: Optional[str]


    class Config:
        schema_extra = {
            "product": {
                "product_id": "123456",
                "productTitle": "Milk for Vegans",
                "productPrice": 123.45,
                "productDescription": "This milk is made by nuts and it's one of the best for vegans"
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
