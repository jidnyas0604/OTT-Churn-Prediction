from flask import Flask, request, jsonify # type: ignore
import joblib#type: ignore
import numpy as np
import pandas as pd
import pymongo # type: ignore
from datetime import datetime

app=Flask(__name__)

model=joblib.load("ott_churn_voting_model.pkl")

MONGO_URI = f"mongodb+srv://<username>:<password>@<Cluster URL>/?retryWrites=true&w=majority&appName=<app name>"

client = pymongo.MongoClient(MONGO_URI)
db = client["Churn_Data"]
collection = db["Churn"]

@app.route('/')
def home():
    return "OTT Churn Prediction API is running"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print("Received data:", data)  # Debugging output

        if "features" not in data:
            return jsonify({"error": "Missing 'features' key"}), 400
        
        features = np.array(data["features"]).reshape(1, -1)
        prediction = model.predict(features)[0]
        # Prepare the data to save in MongoDB
        prediction_data = {
            "features": data["features"],  # Save the input features
            "prediction": int(prediction),  # Save the prediction result
            "timestamp": datetime.utcnow()  # Add a timestamp for when the prediction was made
        }

        # Insert the prediction result into the MongoDB collection
        collection.insert_one(prediction_data)

        return jsonify({"churn_prediction": int(prediction)})
    except Exception as e:
        print("Error:", str(e))  # Debugging output
        return jsonify({"error": str(e)}), 400



    
if __name__ == '__main__':
    app.run(debug=True)







