from fastapi import APIRouter, HTTPException
from internal.models.request_model import RequestModel
from internal.models.data_class import RequestData
from internal.services.prediction_service import get_prediction_result

router = APIRouter()

@router.post("/get_place/")
async def get_place(data: RequestModel):
    """
    Эндпоинт на получение оптимального места размещения рекламы
    """
    # try:
    #     request_data = RequestData(
    #         targetAudience=request.targetAudience,
    #         points=request.points
    #     )
        
    #     prediction = get_prediction_result(request_data)

    #     response = {"prediction": prediction}
    #     return response
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=str(e))
    return {}

@router.get("/status/")
async def get_status():
    return {"status": "ok"}
