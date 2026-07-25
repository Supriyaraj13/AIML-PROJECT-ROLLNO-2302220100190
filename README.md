# Student Performance Prediction 📊

## Project Overview
This project focuses on predicting a student's mathematics score based on various factors such as gender, ethnicity, parental education level, lunch type, test preparation course, reading score, and writing score.

A Machine Learning model using Linear Regression is developed to analyze student performance and identify the factors that influence mathematics scores.

---

## Problem Statement

Schools collect various types of student information including gender, parental education level, lunch type, and test preparation details. The goal of this project is to use this information to predict a student's mathematics score and analyze which factors have the greatest impact on performance.

---

## Business Objective

Educational institutions collect student information such as demographic background, parental education, lunch type, and test preparation status. The objective of this project is to build a regression model that predicts a student's mathematics score and helps identify factors affecting student performance.

This can help educators identify students who may need additional support and make data-driven decisions to improve learning outcomes.

---

## Dataset
Dataset: Students Performance in Exams

Source: Kaggle

The dataset contains information about students' demographic background and exam scores.

---

### Features:
- Gender
- Race/Ethnicity
- Parental level of education
- Lunch type
- Test preparation course
- Reading score
- Writing score

### Target Variable:
- Math score

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

## Project Workflow

1. Data Loading
2. Data Exploration and Understanding
3. Exploratory Data Analysis (EDA)
4. Data Preprocessing
5. Feature Encoding
6. Train-Test Split
7. Linear Regression Model Training
8. Model Evaluation
9. Feature Importance Analysis

---

## Model Performance

The Linear Regression model achieved:

- MAE: 4.21
- RMSE: 5.39
- R² Score: 0.88

The model explains approximately 88% of the variation in mathematics scores.

---

## Key Findings

- Reading and writing scores have a strong positive correlation with mathematics scores.
- Students who completed the test preparation course generally achieved higher math scores.
- Students with standard lunch showed better average mathematics performance compared to free/reduced lunch students.
- Linear Regression coefficient analysis was used to rank the factors influencing mathematics score predictions.
- Correlation analysis was performed to understand relationships between numerical score features.

---

## Project Structure

AIML-Project-RollNo-2302220100190/

├── Dataset/
│   └── StudentsPerformance.csv
│
├── Images/
│   ├── gender_distribution.png
│   ├── correlation_heatmap.png
│   ├── test_preparation.png
│   ├── lunch_vs_math_score.png
│   ├── actual_vs_predicted.png
│   └── feature_importance.png
│
├── Notebook/
│   └── Student_Performance_Prediction.ipynb
│
├── student_performance_model.pkl
│
├── README.md
│
└── requirements.txt

---

## Visualizations

### Gender Distribution

![Gender Distribution](Images/gender_distribution.png)

### Correlation Heatmap

![Correlation Heatmap](Images/correlation_heatmap.png)

### Feature Importance

![Feature Importance](Images/feature_importance.png)

### Actual vs Predicted Scores

![Actual vs Predicted](Images/actual_vs_predicted.png)

### Lunch Type vs Math Score

![Lunch Analysis](Images/lunch_vs_math_score.png)

### Test Preparation vs Math Score

![Test Preparation](Images/test_preparation.png)

---

## Conclusion

This project demonstrates the complete Machine Learning pipeline, from data analysis and preprocessing to model training, evaluation, and feature importance analysis for predicting student performance.