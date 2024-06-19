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
st.title("Bulk Prediction Page 🔮!")

# load the machine learning model components
@st.cache_resource()
def load_ml_components():
    with open("./models/best_models.joblib","rb") as file:
        model_components = joblib.load(file)
    return model_components

# call the load_ml_components function
model_components = load_ml_components()

# load model components
catboost_model = model_components["catboost_model"]
logistic_regressor = model_components["log_regression"]
sgb_classifier = model_components["sgb_classifier"]


# Initialize the session state for the model_name
if "model_name" not in st.session_state:
    st.session_state["model_name"] = "CatBoost"

# select the model to use
col1,col2 = st.columns(2)
with col1:
    model_name = st.selectbox("Select Model",options=["CatBoost","Logistic Regression","SGB"],key="model_name")

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

columns_to_map = ["PaperlessBilling","Partner","Dependents","PhoneService","StreamingMovies","StreamingTV","MultipleLines","OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport"]



#function to get selected model
@st.cache_resource()
def get_selected_model():
    if model_name == "CatBoost":
        pipeline = catboost_model
    elif model_name == "Logistic Regression":
        pipeline = logistic_regressor
    else:
        pipeline = sgb_classifier
    
    # load the encoder
    encoder = model_components["encoder"]
    return pipeline,encoder


def make_bulk_prediction(pipeline,encoder,data):
    # make prediction
    df = pd.DataFrame(data)
    pred = pipeline.predict(df)
    # decode label to original label in the dataset
    decoded_prediction = encoder.inverse_transform(pred.reshape(-1,1))
    # calculate prediction probability 
    probabbility = pipeline.predict_proba(df)
    # probability_label
    prediction_label = ["Yes" if p == 1 else "No" for p in pred]
    # create a dataframe to store the prediction and probability
    df["PredictionTime"] = datetime.date.today()
    df["Prediction"] = prediction_label
    df["PredictionProbability"] = [probabbility[i][p] for i,p in enumerate(pred)]

    return df


if __name__ == "__main__":
    # call the get_selected_model function
    pipeline,encoder = get_selected_model()
    
    # accept data from user
    uploaded_data = st.file_uploader("Upload your CSV data here for prediction",type="csv")

    if uploaded_data is not None:
        data = pd.read_csv(uploaded_data)

        # drop the churn column
        if "Churn" in data.columns:
            data = data.drop(columns="Churn",axis=1)
        # map the values in the columns
        data = values_mapper(data,columns=columns_to_map)
        # convert TotalCharges to numeric datatype
        data["TotalCharges"] = pd.to_numeric(data["TotalCharges"],errors="coerce")
        # map the senior citizen column into Yes or No
        data["SeniorCitizen"] = data["SeniorCitizen"].map({0:"No",1:"Yes"})
        # call the make predictions
        prediction_df = make_bulk_prediction(pipeline,encoder,data)
        st.markdown("### 👇View Prediction Result")
        st.write(prediction_df)
    else:
        st.write("Please upload your data")

   
