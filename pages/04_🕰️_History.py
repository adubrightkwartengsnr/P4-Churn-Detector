import streamlit as st
import pandas as pd


st.set_page_config(
    page_title ='History Page',
    page_icon ='🕰️',
    layout="wide"
)

# load the prediction_history csv
hist_df = pd.read_csv("./data/prediction_history.csv")

st.title("History Page 🕰️")
st.dataframe(hist_df)