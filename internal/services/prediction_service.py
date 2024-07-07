from internal.models.data_class import RequestData
from internal.models.request_model import RequestModel

def preprocess_data(data):
    processed_data = {
        "target_audience": {
            "name": data.targetAudience.name,
            "gender": data.targetAudience.gender,
            "ageFrom": data.targetAudience.ageFrom,
            "ageTo" : data.targetAudience.ageTo,
            "income": data.targetAudience.income,
        },
        "points": [
            {
                "latitude": point.lat,
                "longitude": point.lon,
                "azimuth": point.azimuth,
            }
            for point in data.points
        ]
    }
    return processed_data


def get_prediction_result(data: RequestModel):
    """
    Обработка входных данных
    """
    prepared_data = data.dict()
    
    # prediction = model.predict(prepared_data)
    prediction = "some prediction"
    return prediction
