import streamlit as st
import pandas as pd

st.set_page_config(
    page_title ='History Page',
    page_icon ='🕰️',
    layout="wide"
)

st.title("History Page 🕰️")

# load the prediction_history csv
history_df = pd.read_csv("./data/prediction_history.csv")

# write the history page to user interface
st.dataframe(history_df)
