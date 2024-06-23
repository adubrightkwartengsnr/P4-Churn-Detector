#get libraries
import streamlit as st 
import requests
import json
from streamlit_lottie import st_lottie
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title ='Home Page',
    page_icon ='🏠',
    layout="wide"
)

st.title("ChurnXplorer: Your Number One Power ML model to Cut Customer Churn ✂️")
#define function to get animation
def lottie_url(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_img = lottie_url("https://lottie.host/80d6a368-c787-4f59-8eca-9b649cf41b1b/VdfzfJeXsp.json")


#intro talking about title 
with st.container():
    col1,col2 = st.columns(2)
    with col1:
        st.title("About us")
        st.write("##### We are leading professionals with a diverse portfolio range⭐⭐⭐⭐⭐")
        st.markdown("""
                    ###### Our group of experts in the team operate with the following objectives:

                    - ###### Explore our clients data thoroughly and decide on the most efficient classification models.
                    - ###### Find the lifetime value of each customer and know what factors affect the rate at which customers exit a company.
                    - ###### Predict if a customer will churn or not.""")
    with col2:
           st_lottie(
    lottie_img,
    speed=1,
    reverse= False,
    loop=True,
    quality="high",
    key="coding",
    height=400,
    width=500 )
    

    col1,col2 = st.columns(2)
    with col1:
        st.header("Key Features")
        st.write("""
                    - View Data - Allows you to view data 
                    - Predict - Feature that allows to make single prediction or predict your csv data in bulk
                    - View History - Allows you to view the history of your predictions
                    - Dashboard - View data visualizations
                    """)
        
    with col2:
        st.header("User Benefits")
        st.write("""
                    - Make data driven decisions effortlessly
                    - User-Friendly Interface
                    - Real-Time predictions
                    - Insightful dashboards
                    - Ease to use
                    """)
        
    col1,col2 = st.columns(2)
    with col1:
        st.header("Machine Learning Integration")
        st.write("""
                - You have access three trained machine learning models
                - Simple integration and user-friendly access
                - Save data to local database or locally for future use
                - Get probability of predictions
                """)
    with col2:
        st.header("How To Run Applicattion")
        code = '''
        #Activate Virtual Environment
        source venv/bin/activate

        #Install dependencies
        pip install -r requirements.txt

        #Run the application
        streamlit run app.py
        '''
        st.code(code,language="python")
        

with st.container():
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.header("Contact Me")
        st.write("""
                 contact me at adubrightkwarrteng11@gmail.com for collaborations © 2024. All rights reserved    
        """)
        col3,col4 = st.columns(2)
        with col3:
            st.markdown(f'<a href="https://github.com/adubrightkwartengsnr" target="_blank"><button style="background-color:Red; border:none; border-radius: 5px;">GitHub</button></a>', unsafe_allow_html=True)
            st.markdown(f'<a href="https://www.linkedin.com/in/bright-adu-kwarteng-snr" target="_blank"><button style="background-color:Red; border:none; border-radius: 5px;">LinkedIn</button></a>', unsafe_allow_html=True)
        with col4:
            st.markdown(f'<a href="https://medium.com/@adubrightkwarrteng11" target="_blank"><button style="background-color:Red; border:none; border-radius: 5px;">Medium</button></a>', unsafe_allow_html=True)
            st.markdown(f'<a href="https://drive.google.com/file/d/1q7vbLx-lmm-etNnOyQVvK_WskIxnZmIV/view?usp=drive_link" target="_blank"><button style="background-color:Red; border:none; border-radius: 5px;">Resume</button></a>', unsafe_allow_html=True)
    with col2:
        st.header("Explore")
        st.write("With our powerful machine learning algorithms, you could also try to predict whether a customer will churn or not with you own dataset!")
        data_button = st.button("Predict Here",key="make_prediction")
        if data_button:
            switch_page("Bulk_Predict")  
        
        
        



