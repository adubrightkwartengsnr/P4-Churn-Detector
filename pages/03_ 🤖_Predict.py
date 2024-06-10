import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title ='Predict Page',
    page_icon ='🤖',
    layout="wide"
)
st.title("Predict Churn 🤖!")
# load the machine learning model
@st.cache_resource()
def load_ml_components():
    with open("./models/best_models.joblib","rb") as file:
        model_components = joblib.load(file)
    return model_components

model_components = load_ml_components()

# load model components
catboost_model = model_components["catboost_model"]
logistic_regressor = model_components["log_regression"]
sgb_classifier = model_components["sgb_classifier"]

# initialize the session state

if "selected_model" not in st.session_state:
    st.session_state.selected_model = "Catboost" 
# select a model to use
col1,col2 = st.columns(2)
with col1:
    selected_model = st.selectbox("Select model to predict",
                                                 options=["Catboost","Logistic Regression","SGB"],
                                                 key="selected_model",
                                                 index=["Catboost","Logistic Regression","SGB"].index(st.session_state.selected_model))
st.write("#")
# Update the session state based on the selected model
selected_model = st.session_state.selected_model


# select a model from the select_box
@st.cache_resource(show_spinner="loading models...")
def get_selected_model(selected_model):
    if selected_model == "Catboost":
        pipeline =  catboost_model
    elif selected_model == "Logistic Regression":
        pipeline =  logistic_regressor
    else:
        pipeline =  sgb_classifier

    encoder = model_components["encoder"]
    return pipeline, encoder


# write a function to make prediction
def make_prediction(pipeline,encoder):
    tenure = st.session_state["tenure"]
    monthly_charges = st.session_state["monthly_charges"]
    payment_method = st.session_state["payment_method"]
    contract = st.session_state["contract"]
    paperless_billing = st.session_state["paperless_billing"]
    dependents = st.session_state["dependents"]
    # create rows for the dataframe
    data=[[tenure,monthly_charges,payment_method,contract,paperless_billing,dependents]]
    # create columns for the dataframe
    columns = ["Tenure", "MonthlyCharges","PaymentMethod","Contract","PaperlessBilling","Dependents"]
    df = pd.DataFrame(data=data,columns=columns)
    # make prediction
    pred = pipeline.predict(df)
    pred_int = int(pred[0])

    # transform the predicted variable 
    prediction = encoder.inverse_transform([[pred_int]])[0]

    # calculate prediction probability
    probability = pipeline.predict_proba(df)[0][pred_int]

     # Map probability to Yes or No
    probability_label = "Yes" if pred_int == 1  else "No"
    # update the session state with the prediction and probability
    st.session_state["prediction"] = prediction
    st.session_state["probability_label"] = probability_label
    st.session_state["probability"] = probability
    return prediction,probability_label,probability


if "prediction" not in st.session_state:
    st.session_state.prediction = None

if "probability" not in st.session_state:
    st.session_state.probability = None


# write a function to show the forms to accepts input
def display_forms():
    # call the get_selected_model function
    pipeline,encoder = get_selected_model(st.session_state.selected_model)

    with st.form('input-features'):
        col1,col2 = st.columns(2)
        with col1:
            st.write("## Personal Information 🧑‍💼")
            st.selectbox("Select your gender",options=["Male","Female"],key="gender")
            st.selectbox("Are you a senior citizen?",options=["Yes","No"],key="senior_citizen")
            st.selectbox("Do you have a dependent ?",options=["Yes","No"],key="dependents")
            st.selectbox("Do you have a partner?",options= ["Yes", "No",],key="partner")
            st.number_input("Enter your tenure",min_value = 0, max_value = 72,step=1, key="tenure")
        with col2:
            st.write("### Service Information 🛠️")
            st.number_input("Enter your monthly charges",min_value=0.0, max_value = 200.0,step=0.1, key="monthly_charges")
            st.number_input("Enter you total charges per year",min_value=0,max_value=10000,key="total_charges")
            st.selectbox("Select your payment method",options= ["Electronic check", "Mailed check","Bank transfer (automatic)",
        "Credit card (automatic)"], key="payment_method")
            st.selectbox("Select your prefered contract type",options=["Month-to-month","One year","Two year"],key="contract")
            st.selectbox("Have you subscribed to our Paperless Billing Service?",options=["Yes","No"],key="paperless_billing")
        st.form_submit_button("Make Prediction",on_click=make_prediction,kwargs=dict(pipeline=pipeline,encoder=encoder))



       

if __name__ == "__main__":
    
    # call the display_forms function
    display_forms()

    final_prediction = st.session_state["prediction"]
    if not final_prediction:
        st.write("## Prediction shows here")
        st.divider()
    else:
        # display the prediction result result
        col1,col2 = st.columns(2)
        with col1:
            st.write("### 👇Prediction Results")
            st.write(st.session_state["prediction"])
        with col2:
            st.write("### 🎯Prediction Probability")
            st.write(f"{st.session_state['probability']:.2f}")
    