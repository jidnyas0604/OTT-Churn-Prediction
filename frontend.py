# import streamlit as st # type: ignore
# import requests # type: ignore
# import numpy as np

# # API URL
# # API_URL = "http://127.0.0.1:5000/predict"
# API_URL = "http://localhost:5000/predict"


# # Streamlit UI
# st.title("📺 OTT Churn Prediction")

# # Input fields
# year = st.number_input("Subscription Year", min_value=2000, max_value=2025, value=2015)
# gender = st.selectbox("Gender", ["Male", "Female"])
# watch_time = st.number_input("Total Watch Time (hrs)", min_value=0.0, value=40.0)
# avg_time = st.number_input("Avg Time per Session (mins)", min_value=0.0, value=30.0)
# multi_screen = st.selectbox("Multi-Screen Support", ["Yes", "No"])
# monthly_bill = st.number_input("Monthly Bill ($)", min_value=0.0, value=243.0)
# max_inactive = st.number_input("Max Inactive Days", min_value=0, value=7)
# devices_used = st.number_input("Devices Used", min_value=1, value=3)

# # Convert categorical values
# gender = 1 if gender == "Male" else 0
# multi_screen = 1 if multi_screen == "Yes" else 0

# # Button to predict
# # if st.button("Predict Churn"):
# #     features = [year, gender, watch_time, avg_time, multi_screen, monthly_bill, max_inactive, devices_used]
    
# #     response = requests.post(API_URL, json={"features": features})
    
# #     if response.status_code == 200:
# #         result = response.json()
# #         churn = "Yes" if result["churn_prediction"] == 1 else "No"
# #         st.success(f"📊 Churn Prediction: **{churn}**")
# #     else:
# #         st.error("⚠️ Error in API call!")

# if st.button("Predict Churn"):
#     features = [year, gender, watch_time, avg_time, multi_screen, monthly_bill, max_inactive, devices_used]
    
#     print("Sending JSON:", {"features": features})  # Debugging output
#     response = requests.post(API_URL, json={"features": features})
    
#     if response.status_code == 200:
#         result = response.json()
#         churn = "Yes" if result["churn_prediction"] == 1 else "No"
#         st.success(f"📊 Churn Prediction: **{churn}**")
#     else:
#         st.error(f"⚠️ Error in API call! {response.text}")  # Show response error

import streamlit as st # type: ignore
import requests # type: ignore
import numpy as np

# API URL
API_URL = "http://127.0.0.1:5000/predict"

# Streamlit UI
st.title("Don't Let Your Subscribers Go: OTT Churn Prediction")

# Input fields
year = st.number_input("Subscription Year", min_value=2000, max_value=2025, value=2015)
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=10, max_value=100, value=30)
no_of_days_subscribed = st.number_input("Days Subscribed", min_value=1, value=365)
multi_screen = st.selectbox("Multi-Screen Support", ["Yes", "No"])
watch_time = st.number_input("Total Watch Time (hrs)", min_value=0.0, value=40.0)
avg_time = st.number_input("Avg Time per Session (mins)", min_value=0.0, value=30.0)
weekly_max_night_mins = st.number_input("Weekly Max Night Minutes", min_value=0.0, value=50.0)
max_inactive = st.number_input("Max Inactive Days", min_value=0, value=7)
customer_support_calls = st.number_input("Customer Support Calls", min_value=0, value=1)
devices_used = st.number_input("Devices Used", min_value=1, value=3)
monthly_bill = st.number_input("Monthly Bill ($)", min_value=0.0, value=243.0)

# Convert categorical values
gender = 1 if gender == "Male" else 0
multi_screen = 1 if multi_screen == "Yes" else 0

# Button to predict
if st.button("Predict Churn"):
    features = [
        year, gender, age, no_of_days_subscribed, multi_screen,
        watch_time, avg_time, weekly_max_night_mins, 
        max_inactive, customer_support_calls, devices_used, monthly_bill
    ]
    
    response = requests.post(API_URL, json={"features": features})
    
    if response.status_code == 200:
        result = response.json()
        churn = "Yes" if result["churn_prediction"] == 1 else "No"
        st.success(f"\U0001F4CA Churn Prediction: **{churn}**")
    else:
        st.error("\u26A0\uFE0F Error in API call!")