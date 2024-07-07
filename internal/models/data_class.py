from pydantic import BaseModel
from typing import List

class TargetAudience(BaseModel):
    gender: str
    ageFrom: int
    ageTo: int
    income: str

class RequestData(BaseModel):
    targetAudience: TargetAudience
    tch: List[float]
