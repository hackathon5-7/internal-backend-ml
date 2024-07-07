from pydantic import BaseModel
from typing import List


class TargetAudience(BaseModel):
    gender: str
    ageFrom: int
    ageTo: int
    income: str

class RequestData(BaseModel):
    targetAudience: TargetAudience
    tch: List[int]

    def __repr__(self):
        return f"RequestData(targetAudience={self.targetAudience}, tch={self.tch})"
