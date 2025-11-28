from pydantic import BaseModel, Field
from typing import Optional


class ProductSchema(BaseModel):
    id: Optional[str] = Field(None, description="Product ID")
    name: str = Field(..., description="Product name")
    image_url: str = Field(..., description="Product image")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Product price")
    currency: str = Field(..., description="Product image, USD, MXN")
    in_stock: bool = Field(True, description="Whether the product is in stock")
    category: Optional[str] = Field(None, description="Product category")

    class Config:
        from_attributes = True


class UpdateProductSchema(BaseModel):
    id: Optional[str] = Field(None, description="Product ID")
    name: Optional[str] = Field(None, description="Product name")
    image_url: Optional[str] = Field(None, description="Product image")
    description: Optional[str] = Field(None, description="Product description")
    price: Optional[float] = Field(None, ge=0, description="Product price")
    currency: Optional[str] = Field(None, description="Product image, USD, MXN")
    in_stock: Optional[bool] = Field(None, description="Whether the product is in stock")
    category: Optional[str] = Field(None, description="Product category")

    class Config:
        from_attributes = True