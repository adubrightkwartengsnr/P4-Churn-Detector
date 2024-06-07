import streamlit as st
import pyodbc

st.set_page_config(
    page_title ='Data Page',
    page_icon ='🗄️',
    layout="wide"
)

# create connection to the database and query the database
@st.cache_resource(show_spinner="connecting to database...")
def init_connection():
    pyodbc.connect(
        "DRIVER = {"SQL SERVER"} SERVER=" 
        + st.secrets['server']
        + ";DATABASE=" = st.secrets['database']
        + ";UID=" st.secrets['user']
        + ";PWD=" st.secrets['password'])

# call the init_connection
connection = init_connection()

# querrying the database
@st.cache_data(show_spinner="running query ... ")
def run_query(query):
    with connection.cursor as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
    return rows

sql_query = "SELECT * FROM dbo.LP2_Telco_churn_first_3000"
rows = run_query(sql_query)

