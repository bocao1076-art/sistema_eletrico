import streamlit as st
import pandas as pd
import numpy as np

st.title("Sistema de Cálculo Elétrico")

nome = st.text_input("Nome do equipamento")

potencia = st.number_input(
    "Potência (W)",
    min_value=0.0
)

quantidade = st.number_input(
    "Quantidade",
    min_value=1
)

horas = st.number_input(
    "Horas por dia",
    min_value=0.0
)

if st.button("Calcular"):

    carga_total = potencia * quantidade

    consumo = (
        potencia *
        quantidade *
        horas *
        30
    ) / 1000

    st.success("Cálculo realizado!")

    st.write(
        f"Carga total: "
        f"{carga_total} W"
    )

    st.write(
        f"Consumo mensal: "
        f"{consumo:.2f} kWh"
    )

    dados = pd.DataFrame({
        "Equipamento": [nome],
        "Consumo": [consumo]
    })

    st.dataframe(dados)

    st.bar_chart(dados["Consumo"])
