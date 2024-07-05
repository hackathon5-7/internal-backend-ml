from pydantic import BaseModel

class RequestModel(BaseModel):
    input_data: str
