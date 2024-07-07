from internal.models.data_class import RequestData
from internal.ml.func import func

def preprocess_data(data: RequestData):
    processed_data = {
        "target_audience": {
            "gender": data.targetAudience.gender,
            "ageFrom": data.targetAudience.ageFrom,
            "ageTo": data.targetAudience.ageTo,
            "income": data.targetAudience.income,
        },
        "tch": data.tch
    }
    return processed_data

def get_prediction_result(data: RequestData):
    """
    Обработка входных данных
    """
    prepared_data = preprocess_data(data)
    
    tch = prepared_data["tch"]
    target_audience = prepared_data["target_audience"]
    
    prediction = func(tch, target_audience)
    return prediction
