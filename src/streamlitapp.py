import streamlit as st 
import pandas as pd
import joblib
from utils import prepare, prepare_data_model_2





@st.cache_data
def load_data(path: str):
    df = pd.read_csv(path)
    try:
        df["fechaCreacionLista"] = pd.to_datetime(df["fechaCreacionLista"])
        return df     
    except:
        return df

def main():
    final_data = load_data("../data/cobros_final.csv")
    counts_banks = final_data["idBanco"].value_counts()
    df_final_joined = load_data("../data/df_final_joined_2025.csv")


    st.title("CREDIFIEL  💳 ")

    unique_banks = final_data["idBanco"].unique()
    unique_emisora = final_data["idEmisora"].unique()
    min_date = pd.to_datetime(final_data["fechaCreacionLista"].min()).date()
    max_date = pd.to_datetime(final_data["fechaCreacionLista"].max()).date()

    # st.sidebar.image(r"../images/credifiel.png", width=200)

    st.sidebar.title("Filtros")
    st.sidebar.image(r"../images/credifiel.png", width=200)
    st.sidebar.write("Selecciona el banco")
    bank_selected = st.sidebar.selectbox("idBanco", options=unique_banks, index=0, format_func=lambda x: x)
    st.sidebar.write("Selecciona la emisora")
    emisora_selected = st.sidebar.selectbox("idEmisora", options=unique_emisora, index=0, format_func=lambda x: x)

    st.sidebar.write("Selecciona el rango de Fechas de Creación de Lista ")
    date_range = st.sidebar.slider("fechaCreacionLista", min_value=min_date, max_value=max_date, value=(min_date, max_date), format="YYYY-MM-DD")
    
    start_date = pd.to_datetime(date_range[0])
    end_date = pd.to_datetime(date_range[1])

    filtered_data = final_data[
    (final_data["idBanco"] == bank_selected) &
    (final_data["idEmisora"] == emisora_selected) &
    (final_data["fechaCreacionLista"] >= start_date) & 
    (final_data["fechaCreacionLista"] <= end_date)
]   
    st.write("Predicción de si el cliente pagará el monto o no : ")
    st.write("Ingresa los datos para predecir el comportamiento de pago: ")
    monto_exigible = st.number_input("Monto Exigible model", min_value=0.0, max_value=1000000.0, value=0.0, step=1000.0)
    id_banco = st.selectbox("idBanco model", options=unique_banks)
    id_emisora = st.selectbox("idEmisora model", options=unique_emisora)
    month = st.number_input("Month model", min_value=1, max_value=12, value=1, step=1)
    day = st.number_input("Day model", min_value=1, max_value=31, value=1, step=1)


    model = joblib.load("../models/naive_bayes_model.pkl")

    df = prepare(final_data.copy(), id_banco, id_emisora, monto_exigible, month, day)
    submit_button = st.button("Predecir")

    # st.dataframe(df)
    if submit_button:

        prediction = model.predict(df)
        st.write("Predicción: ", prediction[0])
        st.write("Predicción probabilidad: ", model.predict_proba(df)[0][prediction[0]])
    
    st.write("Predicción de Proporción de pagaré en el 2025: ")


    model2 = joblib.load("../models/xgboostPorcentaje_model.pkl")


    monto_exigible2 = st.number_input("Monto Exigible model 2", min_value=0.0, max_value=1000000.0, value=0.0, step=1000.0)
    monto_cobrar = st.number_input("Monto Cobrar", min_value=0.0, max_value=1000000.0, value=0.0)
    monto_cobrado = st.number_input("Monto Cobrado", min_value=0.0, max_value=1000000.0, value=0.0)
    veces_pagadas = st.number_input("Veces Pagadas", min_value=0, max_value=10000, value=0, step=1)
    total_cobros = st.number_input("Total Cobros", min_value=0, max_value=100, value=0, step=1)
    proporcion_pagos = st.number_input("Proporción Pagos", min_value=0.0, value=0.0, step=0.01)
    pagare = st.number_input("Pagaré", min_value=0.0, value=0.0, step=0.01)
    capital = st.number_input("Capital", min_value=0.0, max_value=1000000.0, value=0.0, step=1000.0)
    month_uc = st.number_input("Mes Último Cobro", min_value=1, max_value=12, value=1, step=1)
    day_uc = st.number_input("Día Último Cobro", min_value=1, max_value=31, value=1, step=1)
    year_uc = st.number_input("Año Último Cobro", min_value=2000, max_value=2100, value=2023, step=1)
    month_fa = st.number_input("Mes Apertura Crédito", min_value=1, max_value=12, value=1, step=1)
    day_fa = st.number_input("Día Apertura Crédito", min_value=1, max_value=31, value=1, step=1)
    year_fa = st.number_input("Año Apertura Crédito", min_value=2000, max_value=2100, value=2023, step=1)

    
    df2 = prepare_data_model_2(df_final_joined.copy(), monto_exigible2, monto_cobrar, monto_cobrado, veces_pagadas, total_cobros, proporcion_pagos, pagare, capital, month_uc, day_uc, year_uc, month_fa, day_fa, year_fa)

    prediction2 = model2.predict(df2)

    submit_button2 = st.button("Predecir 2025")
    if submit_button2:
        st.write("Predicción: ", prediction2[0])



    st.dataframe(filtered_data.head(100))

if __name__ == "__main__":
    main()







