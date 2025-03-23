import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("regmodel.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Streamlit App
st.title("🏡 House Price Prediction App")
st.write("Enter the details below to predict the house price.")

# Input fields
MedInc = st.number_input("Median Income ($1000s)", min_value=0.5, max_value=15.0, step=0.1)
HouseAge = st.number_input("House Age (years)", min_value=1, max_value=100, step=1)
AveRooms = st.number_input("Average Rooms per Household", min_value=1.0, max_value=10.0, step=0.1)
AveBedrms = st.number_input("Average Bedrooms per Household", min_value=0.5, max_value=5.0, step=0.1)
Population = st.number_input("Population in Area", min_value=100, max_value=40000, step=100)
AveOccup = st.number_input("Average Occupancy per Household", min_value=1.0, max_value=10.0, step=0.1)
Latitude = st.number_input("Latitude", min_value=32.0, max_value=42.0, step=0.1)
Longitude = st.number_input("Longitude", min_value=-125.0, max_value=-114.0, step=0.1)

if st.button("Predict Price"):
    input_features = np.array([[MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude]])
    prediction = model.predict(input_features)
    
    st.subheader("Predicted House Price:")
    st.write(f"$ {prediction[0]:,.2f}")

# Footer
st.markdown("---")
st.markdown("Developed with ❤️ using Streamlit")