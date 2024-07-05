from internal.models.data_class import RequestData

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


def get_prediction_result(data: RequestData):
    """
    Обработка входных данных
    """
    prepared_data = preprocess_data(data)
    
    # prediction = model.predict(prepared_data)
    prediction = "some prediction"
    return prediction
