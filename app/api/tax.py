from fastapi import APIRouter
from models.tax import Tax

router = APIRouter()

@router.post("/tax")
async def post_calc(data: Tax):
    in_tax_cost = data.cost * (1 + data.tax_rate)
    return {'税込み価格': in_tax_cost}