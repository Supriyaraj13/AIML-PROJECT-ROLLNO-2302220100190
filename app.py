import streamlit as st
import pickle
import pandas as pd

# Load trained model
with open("student_performance_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🎓 Student Performance Prediction")

st.write(
    "Predict a student's Mathematics Score using the trained Linear Regression model."
)


# Inputs

gender = st.selectbox(
    "Gender",
    ["female", "male"]
)

lunch = st.selectbox(
    "Lunch Type",
    ["free/reduced", "standard"]
)

test_prep = st.selectbox(
    "Test Preparation Course",
    ["none", "completed"]
)

reading = st.number_input(
    "Reading Score",
    min_value=0,
    max_value=100,
    value=70
)

writing = st.number_input(
    "Writing Score",
    min_value=0,
    max_value=100,
    value=70
)


# Prediction

if st.button("Predict Math Score"):

    input_data = {
    "reading_score": reading,
    "writing_score": writing,
    "gender_male": 0 if gender == "male" else 1,
    "lunch_standard": 1 if lunch == "standard" else 0,
    "test_preparation_course_none": 0 if test_prep == "none" else 1
}

    input_df = pd.DataFrame([input_data])

    prediction = model.predict(input_df)

    st.success(
        f"Predicted Mathematics Score: {prediction[0]:.2f}"
    )