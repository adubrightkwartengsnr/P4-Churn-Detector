import streamlit as st
import pyodbc
import pandas as pd
import time
from utils.more_info import markdown_table1
from utils.more_info import markdown_table2
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

st.set_page_config(
    page_title ='Data Page',
    page_icon ='🗄️',
    layout="wide"
)

#### User Authentication
# load the config.yaml file 
with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Create an authentication object
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)
# invoke the login authentication
name, authentication_status, username = authenticator.login(location="sidebar")

if st.session_state["authentication_status"] is None:
    st.warning("Please Log in to get access to the application")
    test_code = '''
    Test Account
    username: brightadu
    password: 1234
    '''
    st.code(test_code)
        
elif st.session_state["authentication_status"] == False:
    st.error("Wrong username or password")
    st.info("Please Try Again")
    test_code = '''
    Test Account
    username: brightadu
    password: 1234
    '''
    st.code(test_code)
else:
    st.info("Login Successful")
    st.write(f'Welcome *{username}*')
    #logout user using streamlit authentication logout
    authenticator.logout('Logout', 'sidebar')

    st.title("Customer Churn Database 🗄️")

    def show_dataframe():
        # read csv
        df = pd.read_csv("./data/telco_churn_full_training.csv")
        # File uploader widget from local directory
        uploaded_file = st.file_uploader("Upload your data", type="csv")
        if uploaded_file is not None:
            df =pd.read_csv(uploaded_file)
        else:
            # load second training data
            df = df.copy()
        return df
    # load dataframe
    df = show_dataframe()

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

    #create a progress bar to let user know data is loading
    progress_bar = st.progress(0)
    for percentage_completed in range(100):
        time.sleep(0.05)
        progress_bar.progress(percentage_completed+1)

    st.success("Data loaded successfully!")

    # initialize the session state for categories
    if "category" not in st.session_state:
        st.session_state["category"] = "All Columns"


    col1,col2 = st.columns(2)
    with col2:
        category = st.selectbox("Choose Category",options=["All Columns","Numerical Columns", "Categorical Columns"],key="category")
    # Filtering Datatypes
    def filter_columns(category):
        if category == "Numerical Columns":
            filtered_df = df.select_dtypes(include="number")
        elif category == "Categorical Columns":
            filtered_df = df.select_dtypes(exclude="number")
        else:
            filtered_df = df
        return filtered_df


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

        # display the filtered dataframe
        st.write(filtered_columns)


    if __name__ == "__main__":
        # call the values_mapper function
        columns_to_map = ["PaperlessBilling","Partner","Dependents","PhoneService","Churn","StreamingMovies","StreamingTV","MultipleLines","OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport"]
        final_df = values_mapper(df,columns=columns_to_map)
       
        

        
    


