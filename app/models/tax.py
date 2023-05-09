from pydantic import BaseModel

class Tax(BaseModel):
    cost: int
    tax_rate: float