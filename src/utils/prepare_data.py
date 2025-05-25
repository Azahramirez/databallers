import numpy as np 
import pandas as pd 
import datetime as dt


def prepare(df: pd.DataFrame, id_banco:str, id_emisora:str, monto_exigible:float, month:int, day:int):  
    """ 
    Prepare data for prediction:

    Args:
        df (pd.DataFrame): DataFrame with the data to prepare.


    """
    df = df[["idBanco", "montoExigible", "idEmisora"]]

    df = pd.get_dummies(df, columns=["idBanco", "idEmisora"], drop_first=True)

    cols = df.columns.tolist()



    cols_index = {}
    for i in range(len(cols)):
        cols_index[cols[i]] = i

    
    df = pd.DataFrame(columns=cols, index=[0]).fillna(False)
    df["idBanco_" + str(id_banco)] = True
    df["idEmisora_" + str(id_emisora)] = True
    df["montoExigible"] = monto_exigible
    df["month"] = month
    df["day"] = day

    return df

def prepare_data_model_2(df:pd.DataFrame, monto_exigible:float, monto_cobrar: float, monto_Cobrado: float, veces_pagadas: int, total_cobros:float, proporcionPagos:float, pagare:float, capital:float, month_uc: int, day_uc:int, year_uc:int, month_fa:int, day_fa:int, year_fa:int):
    """ 
    Prepare data for prediction:
    Args:
        df (pd.DataFrame): DataFrame with the data to prepare.


    """

    df = df.drop(columns=["idCredito", "montoCobrado2025", "proporcionPagada2025"])
    df["ultimoCobro"] = pd.to_datetime(df["ultimoCobro"], format="%d/%m/%Y")
    df["month_uc"] = df["ultimoCobro"].dt.month
    df["day_uc"] = df["ultimoCobro"].dt.day
    df["year_uc"]  = df["ultimoCobro"].dt.year
    df.drop(columns=["ultimoCobro"], inplace=True)
    df["fechaAperturaCredito"] = pd.to_datetime(df["fechaAperturaCredito"], format="%d/%m/%Y")
    df["month_fa"] = df["fechaAperturaCredito"].dt.month
    df["day_fa"] = df["fechaAperturaCredito"].dt.day
    df["year_fa"] = df["fechaAperturaCredito"].dt.year
    df.drop(columns=["fechaAperturaCredito"], inplace=True)


    cols = df.columns.tolist()

    df = pd.DataFrame(columns=cols, index=[0])
    df["montoExigible"] = monto_exigible
    df["montoCobrar"] = monto_cobrar
    df["montoCobrado"] = monto_Cobrado
    df["vecesPagadas"] = veces_pagadas
    df["totalCobros"] = total_cobros
    df["proporcionPagos"] = proporcionPagos
    df["pagare"] = pagare
    df["capital"] = capital
    df["month_uc"] = month_uc
    df["day_uc"] = day_uc
    df["year_uc"] = year_uc
    df["month_fa"] = month_fa
    df["day_fa"] = day_fa
    df["year_fa"] = year_fa

    return df
