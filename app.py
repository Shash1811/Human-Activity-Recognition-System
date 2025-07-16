import streamlit as st
import pandas as pd
import joblib  # Use joblib instead of pickle

# Load model and feature list using joblib
model = joblib.load('har_model.pkl')  # Correct model filename
feature_names = joblib.load('features.pkl')  # Ensure you saved features.pkl too

# Streamlit App
st.title("Human Activity Recognition App 🕺📱")

st.write("Upload a CSV file with sensor data to predict activities.")

uploaded_file = st.file_uploader("Upload test CSV", type="csv")

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    
    # Check if all required features are present
    if set(feature_names).issubset(data.columns):
        X_test = data[feature_names]

        # Make predictions
        predictions = model.predict(X_test)
        data['Predicted Activity'] = predictions

        st.success("Predictions completed! ✅")
        st.write(data.head())

        # Optional: plot activity distribution
        st.subheader("📊 Activity Count")
        st.bar_chart(data['Predicted Activity'].value_counts())
    else:
        st.error("Uploaded file is missing some required features.")
