from pydantic import BaseModel
from typing import List

class RequestData(BaseModel):
    gender: str
    ageFrom: int
    ageTo: int
    income: str
    tch: List[int]
