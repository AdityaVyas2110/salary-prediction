import pickle
import pandas as pd

# Load saved model
with open("../model/salary_model.pkl", "rb") as f:
    model = pickle.load(f)

# New employee data
data = pd.DataFrame({
    "experience": [3],
    "age": [29],
    "education": ["Master"],
    "city": ["Delhi"]
})

# Predict salary
prediction = model.predict(data)

print("Predicted Salary:", prediction[0])
