Employee Salary Prediction using Machine Learning

 Project Overview

This project predicts an employee's salary based on features such as experience, age, education level, and city using a classical machine learning regression model.

The goal of this project is to demonstrate a complete machine learning workflow, including data preprocessing, model training, evaluation, and prediction.

---

 Features

- Data preprocessing with One-Hot Encoding
- Machine Learning model using Linear Regression
- Train/Test dataset splitting
- Model evaluation using Mean Absolute Error
- Model saving and loading using Pickle
- Salary prediction for new employee data

---

 Machine Learning Concepts Used

- Data preprocessing
- Feature encoding
- Train/Test split
- Regression modeling
- Model evaluation
- Model persistence

---

 Project Structure

salary-prediction

│

├── data
│   └── salary_data.csv

├── src
│   ├── train.py
│   └── predict.py

├── model
│   └── salary_model.pkl

├── requirements.txt
└── README.md

---

 Dataset

The dataset contains the following columns:

Feature| Description
experience| Years of work experience
age| Employee age
education| Education level (Bachelor, Master, PhD)
city| Work location
salary| Target variable (employee salary)

---

 Installation

Clone the repository

git clone https://github.com/yourusername/salary-prediction-ml.git

Navigate to the project directory

cd salary-prediction-ml

Install dependencies

pip install -r requirements.txt

---

 Train the Model

Run the training script:

python src/train.py

This will:

- Train the machine learning model
- Evaluate performance
- Save the model in the model/ directory

---

 Make Predictions

Run the prediction script:

python src/predict.py

Example Output:

Predicted Salary: 47000

---
 Requirements

- Python 3.x
- pandas
- scikit-learn

Install them using:

pip install -r requirements.txt

---

 Model Used

Linear Regression

Evaluation metric:

Mean Absolute Error (MAE)

---

 Future Improvements

- Add more machine learning models (Random Forest, Gradient Boosting)
- Perform exploratory data analysis (EDA)
- Deploy the model using Flask or FastAPI
- Build a simple web interface for predictions

---

 Author

Aditya Vyas

GitHub: https://github.com/AdityaVyas2110

---

⭐ If you like this project, consider giving it a star!
