from fastapi import APIRouter
from typing import List
# from db.models.sample import Sample

from typing import Optional
from pydantic import BaseModel

class Sample(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

router = APIRouter()

@router.get("/samples", response_model=List[Sample])
async def read_samples():
    return [
        {"id": 1, "name": "sample1", "description": "description1"},
        {"id": 2, "name": "sample2", "description": "description2"},
        {"id": 3, "name": "sample3","description": "description3"}
    ]
