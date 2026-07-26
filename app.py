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

# ---------------- INPUTS ----------------

gender = st.selectbox("Gender", ["female", "male"])

race = st.selectbox(
    "Race/Ethnicity",
    ["group A", "group B", "group C", "group D", "group E"]
)

parent = st.selectbox(
    "Parental Level of Education",
    [
        "associate's degree",
        "bachelor's degree",
        "high school",
        "master's degree",
        "some college",
        "some high school"
    ]
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

# ---------------- PREDICTION ----------------

if st.button("Predict Math Score"):

    data = {
        "reading_score": reading,
        "writing_score": writing,
        "test_prep_completed": 1 if test_prep == "completed" else 0,
        "gender_male": 1 if gender == "male" else 0,

        "race_ethnicity_group B": 1 if race == "group B" else 0,
        "race_ethnicity_group C": 1 if race == "group C" else 0,
        "race_ethnicity_group D": 1 if race == "group D" else 0,
        "race_ethnicity_group E": 1 if race == "group E" else 0,

        "parental_level_of_education_bachelor's degree":
            1 if parent == "bachelor's degree" else 0,

        "parental_level_of_education_high school":
            1 if parent == "high school" else 0,

        "parental_level_of_education_master's degree":
            1 if parent == "master's degree" else 0,

        "parental_level_of_education_some college":
            1 if parent == "some college" else 0,

        "parental_level_of_education_some high school":
            1 if parent == "some high school" else 0,

        "lunch_standard":
            1 if lunch == "standard" else 0,

        "test_preparation_course_none":
            1 if test_prep == "none" else 0,
    }

    input_df = pd.DataFrame([data])

    prediction = model.predict(input_df)

    st.success(f"Predicted Mathematics Score: {prediction[0]:.2f}")