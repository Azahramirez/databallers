from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import joblib
import pandas as pd 
from input_data import InputData



model = joblib.load("../models/naive_bayes_model.pkl")
app = FastAPI()

@app.post("/predict/{model_name}")
def predict(model_name: str, data: InputData) -> int:
    """ 
    Predic whether a person is a good or bad payer
    Args:
        model_name (str): name of the model
        data (dict): data to predict
    # """
    df = pd.DataFrame([data.dict()])
    df = pd.get_dummies(df, columns=["idBanco", "idEmisora"], drop_first=True)    
    prediction = model.predict([[data.montoExigible, data.pay, data.idBanco, data.idEmisora, data.month, data.day]])
    return {"prediction": int(prediction[0])}    











