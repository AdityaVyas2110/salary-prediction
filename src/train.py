import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Load dataset
data = pd.read_csv("../data/salary_data.csv")

# Features and target
X = data.drop("salary", axis=1)
y = data["salary"]

# Categorical columns
categorical_features = ["education", "city"]

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(), categorical_features)
    ],
    remainder="passthrough"
)

# Pipeline
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model.fit(X_train, y_train)

# Prediction
preds = model.predict(X_test)

# Evaluate model
mae = mean_absolute_error(y_test, preds)
print("Mean Absolute Error:", mae)

# Save model using pickle
with open("../model/salary_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully!")
