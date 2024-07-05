from pydantic import BaseModel
from typing import List

class TargetAudience(BaseModel):
    name: str
    gender: str
    ageFrom: int
    ageTo: int
    income: str

class Point(BaseModel):
    lat: str
    lon: str
    azimuth: int

class RequestModel(BaseModel):
    targetAudience: TargetAudience
    points: List[Point]
