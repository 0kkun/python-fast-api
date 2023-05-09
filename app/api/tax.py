from fastapi import APIRouter
# from db.models.tax import Tax

from pydantic import BaseModel

class Tax(BaseModel):
    cost: int
    tax_rate: float

router = APIRouter()

@router.post("/tax")
async def post_calc(data: Tax):
    in_tax_cost = data.cost * (1 + data.tax_rate)
    return {'税込み価格': in_tax_cost}