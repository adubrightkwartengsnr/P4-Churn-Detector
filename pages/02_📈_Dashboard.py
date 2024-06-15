import streamlit as st
import plotly.express as xp

st.set_page_config(
    page_title ='Dashboard Page',
    page_icon ='📈',
    layout="wide"
)






if __name__ == "__main__":
    # set page title
    st.title("Dashboard Page📈")
    col1,col2 = st.columns(2)
    with col1:
        pass
    with col2:
        st.selectbox("Select Dashboard Type",options=["EDA","KPI"],key="selected_dashboard_type")
