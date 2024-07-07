from pydantic import BaseModel
from typing import List

class RequestData(BaseModel):
    gender: str
    ageFrom: int
    ageTo: int
    income: str
    tch: List[int]

    def __repr__(self):
        return f"RequestData(gender={self.gender}, ageFrom={self.ageFrom}, ageTo={self.ageTo}, income={self.income}, tch={self.tch})"
