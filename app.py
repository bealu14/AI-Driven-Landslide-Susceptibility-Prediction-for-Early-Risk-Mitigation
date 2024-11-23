import streamlit as st
import pandas as pd
import joblib


model = joblib.load('landslide_model.pkl')

st.title('Group 11')
st.title('Landslide Prediction Model')


aspect = st.number_input('Aspect', value=0, min_value=0)
curvature = st.number_input('Curvature', value=0, min_value=0)
earthquake = st.number_input('Earthquake', value=0, min_value=0)
elevation = st.number_input('Elevation', value=0, min_value=0)
flow = st.number_input('Flow', value=0, min_value=0)
lithology = st.number_input('Lithology', value=0, min_value=0)
ndvi = st.number_input('NDVI', value=0.0, format="%.2f")
ndwi = st.number_input('NDWI', value=0.0, format="%.2f")
plan = st.number_input('Plan', value=0, min_value=0)
precipitation = st.number_input('Precipitation', value=0.0, format="%.2f")
profile = st.number_input('Profile', value=0, min_value=0)
slope = st.number_input('Slope', value=0, min_value=0)


input_data = pd.DataFrame({
    'Aspect': [aspect],
    'Curvature': [curvature],
    'Earthquake': [earthquake],
    'Elevation': [elevation],
    'Flow': [flow],
    'Lithology': [lithology],
    'NDVI': [ndvi],
    'NDWI': [ndwi],
    'Plan': [plan],
    'Precipitation': [precipitation],
    'Profile': [profile],
    'Slope': [slope]
})


if st.button('Predict'):
    prediction = model.predict(input_data)
    st.write(f'Prediction: {"Landslide" if prediction[0] == 1 else "No Landslide"}')
