from pydantic import BaseModel


class ProductResponse(BaseModel):
    id: int
    title: str
    price: float
    category: str