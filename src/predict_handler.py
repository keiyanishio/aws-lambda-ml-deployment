import json
import pickle
import pandas as pd


def load_model():
    with open("model.pkl", "rb") as file:
        return pickle.load(file)


def load_ohe():
    with open("ohe.pkl", "rb") as file:
        return pickle.load(file)


def predict_handler(event, context):
    ohe = load_ohe()
    model = load_model()
    event_body = json.loads(event["body"])
    data = pd.DataFrame([event_body], index=[0])
    encoded = ohe.transform(data)
    prediction = model.predict(encoded)[0]
    return {"statusCode": 200, "body": json.dumps({"prediction": str(prediction)})}
