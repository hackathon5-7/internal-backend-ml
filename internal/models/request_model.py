from pydantic import BaseModel
from typing import List, Optional

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
    gender: str
    ageFrom: int
    ageTo: int
    income: str
    count_point_on_segment: list
