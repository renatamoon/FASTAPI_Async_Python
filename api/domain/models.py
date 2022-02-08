from pydantic import BaseModel, Field


# Model of the class Product
class ProductSchema(BaseModel):
    id: int
    productTitle: str = Field(min_length=2)
    productPrice: float = Field(min_length=1)
    productDescription: str = Field(min_length=4)


    class Config:
        extra : "forbid"
        schema_extra = {
            "product_schema": {
                "id": 123456,
                "productTitle": "ventilator",
                "productPrice": 120.00,
                "productDescription": "Ventilator for home usage, Color: Blue"
            }
        }

