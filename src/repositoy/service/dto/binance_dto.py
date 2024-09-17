from pydantic import BaseModel

class BinanceGetDTO(BaseModel):
    title: str
    min_price: float
    max_price: float 
    difference: float
    total_amount: float