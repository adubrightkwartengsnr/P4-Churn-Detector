import os
import streamlit as st
import pandas as pd
import joblib
import datetime

st.set_page_config(
    page_title ='Bulk Predict Page',
    page_icon ='🔮',
    layout="wide"
)
st.title("Bulk Predict Churn 🔮!")