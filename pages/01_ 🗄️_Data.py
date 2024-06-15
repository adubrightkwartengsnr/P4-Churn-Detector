import streamlit as st
import pyodbc
import pandas as pd
import time
from utils.more_info import markdown_table1
from utils.more_info import markdown_table2

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
# connection = init_connection()

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
    # load second training data
    df1 = pd.read_csv("./data/LP2_Telco-churn-second-2000.csv")
    df2 = get_all_columns()
    train_df = pd.concat([df1,df2])
    


def values_mapper(df,columns):
    """ This function takes two parameters and map the values in the column
    df: dataframe object
    columns_columns: columnsin in the dataframe that you want to map the values
    returns dataframe
    """
    for col in columns:
        cat_mapping = {True:"Yes",False:"No","No internet service":"No","No phone service":"No"}
        df[col] = df[col].replace(cat_mapping)
    return df

columns_to_map = ["PaperlessBilling","Partner","Dependents","PhoneService","Churn","StreamingMovies","StreamingTV","MultipleLines","OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport"]
train_df = values_mapper(train_df,columns=columns_to_map)

#create a progress bar to let user know data is loading
progress_bar = st.progress(0)
for percentage_completed in range(100):
    time.sleep(0.05)
    progress_bar.progress(percentage_completed+1)

st.success("Data loaded successfully!")

# initialize the session state for categories
if "category" not in st.session_state:
    st.session_state["category"] = "All Columns"

# initialize the session state for show_info
# if "show_info" not in st.session_state:
#     st.session_state["show_info"] = False


col1,col2 = st.columns(2)
with col2:
    category = st.selectbox("Choose Category",options=["All Columns","Numerical Columns", "Categorical Columns"],key="category")
# Filtering Datatypes
def filter_columns(category):
    if category == "Numerical Columns":
        filtered_df = train_df.select_dtypes(include="number")
    elif category == "Categorical Columns":
        filtered_df = train_df.select_dtypes(exclude="number")
    else:
        filtered_df = train_df
    return filtered_df

# def show_info_button_handler():
    # st.session_state["show_info"] = not st.session_state["show_info"] 

# show info button
show_info = st.button("Click here to view information about data",key="show_info")
    
# Filter markdowns based on the selected columns category
if show_info:
    if st.session_state["category"] == "Numerical Columns":
        st.write("Numerical Columns")
        st.markdown(markdown_table1)
    elif st.session_state["category"] == "Categorical Columns":
        st.write("Categorical Columns")
        st.markdown(markdown_table2)
    else:
        col1,col2 = st.columns(2)
        with col1:
            st.write("Numerical Columns")
            st.markdown(markdown_table1)
        with col2:
            st.write("Categorical Columns")
            st.markdown(markdown_table2)
else:
    st.write("#")
    filtered_columns = filter_columns(st.session_state.category)

     # call the show_info_button_handler
    # show_info_button_handler()

    # display the filtered dataframe
    st.write(filtered_columns)


if __name__ == "__main__":

    # call the init_connection
    connection = init_connection()

    # call the get_all_columns function
    get_all_columns()
    
    # call the values_mapper function
    columns_to_map = ["PaperlessBilling","Partner","Dependents","PhoneService","Churn","StreamingMovies","StreamingTV","MultipleLines","OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport"]
    train_df = values_mapper(train_df,columns=columns_to_map)
     # display the filtered 
    
   


