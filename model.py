import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("data/crop_data.csv")

# Split data
X = df.drop("label", axis=1)
y = df["label"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Prediction function
def predict_crop(input_data):
    prediction = model.predict([input_data])
    return prediction[0]