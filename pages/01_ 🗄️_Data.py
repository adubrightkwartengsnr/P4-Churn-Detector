import streamlit as st
import pyodbc
import pandas as pd

st.set_page_config(
    page_title ='Data Page',
    page_icon ='🗄️',
    layout="wide"
)


st.title("Customer Churn Database 🗄️")


# create connection to the database and query the database
@st.cache_resource(show_spinner="connecting to database...")
def init_connection():                                                         
     return pyodbc.connect(
        f"DRIVER={{SQL Server}};SERVER={st.secrets['server']};DATABASE={st.secrets['database']};UID={st.secrets['username']};PWD={st.secrets['password']}"
    )
# call the init_connection
connection = init_connection()

# querrying the database
@st.cache_data(show_spinner="running query ... ")
def run_query(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        df = pd.DataFrame.from_records(rows, columns=[col[0] for col in cursor.description])
    return df

@st.cache_data(show_spinner="running query... ")
def get_all_columns():
    sql_query = "SELECT * FROM dbo.LP2_Telco_churn_first_3000"
    df = run_query(sql_query)
    return df


# File uploader widget from local directory
uploaded_file = st.file_uploader("Upload your data", type="csv")
if uploaded_file is not None:
    df =pd.read_csv(uploaded_file)
else:
    df = get_all_columns()
    

col1,col2 = st.columns(2)
with col2:
    category = st.selectbox("Choose Category",options=["All Columns","Numerical Columns", "Categorical Columns"])

# Filtering Datatypes
if category == "Numerical Columns":
    filtered_df = df.select_dtypes(include="number")
elif category == "Categorical Columns":
    filtered_df = df.select_dtypes(exclude="number")
else:
    filtered_df = df

# display the filtered dataframe
st.write(filtered_df)

