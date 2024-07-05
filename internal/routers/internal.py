from fastapi import APIRouter, HTTPException
from internal.models.request_model import RequestModel
from internal.services.prediction_service import get_prediction_result

router = APIRouter()

@router.post("/get_place")
def get_place(request: RequestModel):
    try:
        input_data = request.input_data
        print(input_data)
        
        prediction = get_prediction_result(input_data)
        
        response = {"prediction": prediction}
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/status")
def get_status():
    return {"status": "ok"}
