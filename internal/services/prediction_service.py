from internal.models.data_class import RequestData
from internal.ml.func import func

def preprocess_data(data: RequestData):
    processed_data = {
        "gender": data.gender,
        "ageFrom": data.ageFrom,
        "ageTo": data.ageTo,
        "income": data.income,
        "tch": data.tch
    }
    return processed_data


def get_prediction_result(data: RequestData):
    """
    Обработка входных данных
    """
    prepared_data = preprocess_data(data)
    
    tch = prepared_data["tch"]
    target_audience = {
        "gender": prepared_data["gender"],
        "ageFrom": prepared_data["ageFrom"],
        "ageTo": prepared_data["ageTo"],
        "income": prepared_data["income"]
    }
    
    prediction = func(tch, target_audience)
    
    return prediction
