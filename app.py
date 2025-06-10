import streamlit as st
import pandas as pd

st.title("Football Forecasting AI")
match = st.sidebar.selectbox("Match", ["Amazonas vs. Athletic Club"])
if match == "Amazonas vs. Athletic Club":
    st.write("Predicted: Amazonas 1-0 (42% ±5%)")
    df = pd.read_csv("data/match_data.csv")
    st.write(df)