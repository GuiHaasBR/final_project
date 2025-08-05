# app.py
import streamlit as st
import pandas as pd
import joblib

df3 = pd.read_csv('df3.csv')
features = df3.drop(columns = ["price",'property_type','neighborhood','city'])

# Carregar modelo treinado
model = joblib.load("model.pkl")

st.title("🏘️ Barcelona Price Estimator")

# Inputs
sq_m_built = st.number_input("Size in m²", min_value=20, max_value=300)
n_bedrooms = st.selectbox("Bedrooms", [1, 2, 3, 4])
bathrooms = st.selectbox("Bathrooms", [1, 2])
floor = st.slider("Floor", 0, 10)
year_built = st.number_input("Year Built", min_value=1900, max_value=2025)

# Extras (booleans)
lift = st.checkbox("Lift")
terrace = st.checkbox("Terrace")
air_conditioning = st.checkbox("Air Conditioning")

# Categóricas
property_type = st.selectbox("Property Type", ['Flat / apartment', 'Penthouse', 'Studio'])
city = st.selectbox("City", df3['city'].dropna().unique())
neighborhood = st.selectbox("Neighborhood", df3[df3['city'] == city]['neighborhood'].unique())

if st.button("Estimate Price"):
    input_df = pd.DataFrame([{
        'sq_m_built': sq_m_built,
        'n_bedrooms': n_bedrooms,
        'bathrooms': bathrooms,
        'floor': floor,
        'year_built': year_built,
        'lift': int(lift),
        'terrace': int(terrace),
        'air_conditioning': int(air_conditioning),
        'property_type': property_type,
        'city': city,
        'neighborhood': neighborhood
    }])

    price = model.predict(input_df)[0]
    st.success(f"💰 Estimated Price: €{int(price):,}")
