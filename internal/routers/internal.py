from fastapi import APIRouter, HTTPException
from internal.models.data_class import RequestData
from internal.services.prediction_service import get_prediction_result

router = APIRouter()

@router.post("/get_place/")
async def get_place(data: RequestModel):
    """
    Эндпоинт на получение оптимального места размещения рекламы
    """
    try:
         request_data = RequestData(
            gender=data.gender,
            ageFrom=data.ageFrom,
            ageTo=data.ageTo,
            income=data.income,
            tch=data.tch
        )
        value = get_prediction_result(data)
        response = {"value": value}
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {}

@router.get("/status/")
async def get_status():
    return {"status": "ok"}
