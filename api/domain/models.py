from pydantic import BaseModel


# Model of the class Product
class ProductSchema(BaseModel):
    id: int
    productTitle: str
    productPrice: float
    productDescription: str

    class Config:
        extra : "forbid"
        
        # schema_extra = {
        #    "product_schema": {
        #        "id": 123456,
        #        "productTitle": "ventilator",
        #        "productPrice": 120.00,
        #        "productDescription": "Ventilator for home usage, Color: Blue"
        #    }
        #}
