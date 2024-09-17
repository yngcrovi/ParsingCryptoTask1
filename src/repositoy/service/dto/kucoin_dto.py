from pydantic import BaseModel

class KucoinGetDTO(BaseModel):
    title: str
    min_price: float
    max_price: float 
    difference: float
    total_amount: float