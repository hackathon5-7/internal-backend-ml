from internal.models.request_model import TargetAudience, Point
from typing import List

class RequestData:
    def __init__(self, targetAudience: TargetAudience, points: List[Point]):
        self.targetAudience = targetAudience
        self.points = points

    def __repr__(self):
        return f"RequestData(targetAudience={self.targetAudience}, points={self.points})"
