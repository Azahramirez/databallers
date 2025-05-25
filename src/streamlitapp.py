import streamlit as st 
import pandas as pd


@st.cache_data
def load_data(path: str):
    df = pd.read_csv(path)
    df["fechaCreacionLista"] = pd.to_datetime(df["fechaCreacionLista"])
    return df     

def main():
    final_data = load_data("data/cobros_final.csv")
    counts_banks = final_data["idBanco"].value_counts()


    st.title("CREDIFIEL  💳 ")

    unique_banks = final_data["idBanco"].unique()
    unique_emisora = final_data["idEmisora"].unique()
    min_date = pd.to_datetime(final_data["fechaCreacionLista"].min()).date()
    max_date = pd.to_datetime(final_data["fechaCreacionLista"].max()).date()
    # st.sidebar.image(r"../images/credifiel.png", width=200)

    st.sidebar.title("Filtros")
    st.sidebar.image(r"images/credifiel.png", width=200)
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

    st.dataframe(filtered_data.head(100))

if __name__ == "__main__":
    main()







