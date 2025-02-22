import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler,LabelEncoder

def load_model():
    with open("student_lr_final.pkl",'rb') as file:
        model,scaler,le=pickle.load(file)
    return model,scaler,le

def preprocessing_input_data(data,scaler,le):
    data['Extracurricular Activities']=le.transform([data['Extracurricular Activities']])
    df=pd.DataFrame([data])
    df_transformed=scaler.transform(df)
    return df_transformed


def predict_data(data):
    model,scaler,le=load_model()
    processed_data=preprocessing_input_data(data,scaler,le)
    prediction=model.predict(processed_data)
    return prediction

def main():
    st.title("Student Performance Prediction")
    st.write("Enter Your data to get a prediction for your performance")

    hour_std=st.number_input("Hours Studied",min_value=1,max_value=10,value=5)
    prev_score=st.number_input("Previous Score",min_value=0,max_value=100)
    extra_curr=st.selectbox("Extra curricular Activity",["Yes","No"])
    sleeping_hour=st.number_input("Sleeping Hour",min_value=0,max_value=24)
    number_of_paper_solved=st.number_input("Number of question Paper Solved",min_value=0,max_value=5)
    if st.button("predict your score"):
        user_data={
            "Hours Studied":hour_std,
            "Previous Scores":prev_score,
            "Extracurricular Activities":extra_curr,
            "Sleep Hours":sleeping_hour,
            "Sample Question Papers Practiced":number_of_paper_solved
        }
        prediction=predict_data(user_data)
        st.success(f"your prediction result is {prediction}")
    
if __name__=="__main__":
    main()