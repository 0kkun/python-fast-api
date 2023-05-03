from typing import Optional
from pydantic import BaseModel

class Sample(BaseModel):
    id: int
    name: str
    description: Optional[str] = None