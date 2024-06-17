import streamlit as st
import plotly.express as px
import pandas as pd


st.set_page_config(
    page_title ='Dashboard Page',
    page_icon ='📈',
    layout="wide"
)

# read data for dashboard
df = pd.read_csv("./data/telco_churn_full_training.csv")


# Create a function to view the EDA
def eda_dashboard():
    st.markdown("### Exploratory Data Analysis ")
    st.write("#")
    st.markdown("#### Univariate Analysis")
    # manually set color map
    color_map = {"Yes":"pink","No":"green"}
    col1,col2 = st.columns(2)
    with col1:
        monthlycharges_histogram = px.histogram(df,x="MonthlyCharges",title="Distribution of MonthlyCharges")
        st.plotly_chart(monthlycharges_histogram)
    with col2:
        totalcharges_histgram = px.histogram(df,x="TotalCharges",title="Distribution of TotalCharges")
        st.plotly_chart(totalcharges_histgram)

    col3,col4 = st.columns(2)
    with col3:
        # plot a histogram of Tenure
        tenure_histogram = px.histogram(df,x="Tenure",title="Distribution of Tenure")
        st.plotly_chart(tenure_histogram)
    with col4:
        pieplot = px.pie(df,names="Churn",title="Churn by InternetService",color="Churn",color_discrete_map=color_map,hole=0.3)
        st.plotly_chart(pieplot)
        
    col5,col6 = st.columns(2)
    with col5:
        boxplot = px.box(df,x="TotalCharges",title="BoxPlot of TotalCharges")
        st.plotly_chart(boxplot)
    with col6:
        boxplot = px.box(df,x="Tenure",title="BoxPlot of Tenure")
        st.plotly_chart(boxplot)

    boxplot = px.box(df,x="MonthlyCharges",title="Boxplot of MonthlyCharges")
    st.plotly_chart(boxplot)


    
    st.write("#")
    st.markdown("#### Bivariate Analysis")
    col1,col2 = st.columns(2)
    with col1:
        boxplot = px.box(df,x="MonthlyCharges",y="Churn",title="Distribution of Churn by MonthlyCharges")
        st.plotly_chart(boxplot)
    with col2:
        boxplot = px.box(df,x="TotalCharges",y="Churn",title="Distribution of Churn by TotalCharges")
        st.plotly_chart(boxplot)

    col3,col4 = st.columns(2)
    with col3:
        boxplot = px.box(df,x="Tenure",y="Churn",title="Distribution of Churn by Tenure")
        st.plotly_chart(boxplot)
    with col4:
        barplot = px.bar(df,x="InternetService",y="MonthlyCharges",color="Churn",color_discrete_map=color_map)
        st.plotly_chart(barplot)
            

    st.write("#")
    st.markdown("#### Multivariate Analysis")
    col1,col2 = st.columns(2)
    with col1:
        scatter_plot = px.scatter(df,x="MonthlyCharges",y="TotalCharges",color="Churn",color_discrete_map=color_map,title="Relation Between Churn and Charges")
        st.plotly_chart(scatter_plot)
    with col2:
        numerical_data = df.select_dtypes("number")
        numerical_data.drop(columns=["Unnamed: 0"],inplace=True)
        cor_matrix = numerical_data.corr()
        heat_map = px.imshow(cor_matrix,text_auto=True,aspect="auto",title="Correlation Matrix")
        st.plotly_chart(heat_map)
       


def kpi_dashboard():
    st.markdown(" ### Key Performance Index")





if __name__ == "__main__":
    # set page title
    st.title("Dashboard Page📈")

    col1,col2 = st.columns(2)
    with col1:
        pass
    with col2:
        st.selectbox("Select Dashboard Type",options=["EDA","KPI"],key="selected_dashboard_type")

    if st.session_state.selected_dashboard_type == "EDA":
        eda_dashboard()
    else:
        kpi_dashboard()
