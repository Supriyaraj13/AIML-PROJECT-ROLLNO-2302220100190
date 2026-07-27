# Student Performance Prediction 📊

## 🚀 Live Demo

Streamlit Application:  
https://student-performance-prediction-sr.streamlit.app/

---

## Problem Statement

The objective of this project is to predict a student's mathematics score using demographic and academic information.

The project analyzes factors such as gender, lunch type, test preparation course, reading score, and writing score to understand student performance.

A Machine Learning regression model using **Linear Regression** is developed to predict mathematics scores based on these factors.

---

## Dataset

- **Name:** Students Performance in Exams
- **Source:** Kaggle
- **Link:** https://www.kaggle.com/datasets/spscientist/students-performance-in-exams
- **Dataset Size:** 1000 rows and 8 columns

The dataset contains information about students' demographic background and academic performance.

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

## Tools & Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Streamlit

---

## Project Workflow

1. Data Collection
2. Data Cleaning and Validation
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Categorical Data Encoding
6. Train-Test Split
7. Model Training using Linear Regression
8. Model Evaluation
9. Feature Importance Analysis
10. Model Deployment using Streamlit

---

## Model Performance

### Machine Learning Model

**Model Used:** Linear Regression

### Evaluation Metrics:

- **MAE:** 4.21
- **RMSE:** 5.39
- **R² Score:** 0.88

The model explains approximately **88% of the variation** in students' mathematics scores.

---

## Key Insights

- Reading and writing scores show a strong positive relationship with mathematics scores.
- Students who completed the test preparation course generally achieved better math scores.
- Lunch type shows an association with student performance.
- Linear Regression coefficients were used to understand the contribution of different features toward prediction.

---

## Project Structure

```
AIML-Project-RollNo-2302220100190/

│
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
├── app.py
│
├── student_performance_model.pkl
│
├── README.md
│
└── requirements.txt
```

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

## Future Improvements

- Try different Machine Learning algorithms and compare performance.
- Improve prediction accuracy using advanced models.
- Add more relevant student-related features.
- Enhance the Streamlit application interface.

---

## Conclusion

This project demonstrates an end-to-end Machine Learning workflow for predicting student mathematics performance.

The process includes data cleaning, exploratory data analysis, feature engineering, categorical encoding, model training, evaluation, and deployment.

The Linear Regression model achieved an R² score of approximately **0.88**, showing that academic factors such as reading and writing scores are strong indicators of mathematics performance.

---

## Author

**Supriya Raj**