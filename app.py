import streamlit as st
import pandas as pd
import pickle
import numpy as np

with open(r"C:\Users\User\Desktop\IronHack\Week_8\Day1\final_project\models\best_model.pkl", "rb") as file:
    model = pickle.load(file) 

with open(r"C:\Users\User\Desktop\IronHack\Week_8\Day1\final_project\scalers\scaler_novo.pkl", "rb") as file:
    scaler = pickle.load(file)

city_map = {
    'Barcelona': 5,
    'Badalona': 4,
    'Hospitalet': 3,
    'Sabadell': 2,
    'Terrassa': 1
}

st.title("🏘️ Barcelona Price Estimator")

model_features = ['city','sq_m_built', 'n_bedrooms', 'bathrooms', 'floor', 'year_built',
                  'exterior', 'lift', 'terrace', 'balcony', 'second_hand',
                  'needs_renovating', 'parking', 'swimming_pool', 'garden',
                  'air_conditioning', 'heating', 'price_cheap_city',
                  'price_cheap_neigh', 'price_cheap_property']

sq_m_built = st.number_input("Size in m²", min_value=20, max_value=1000, value=80)
n_bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=2)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=5, value=1)
floor = st.select_slider("Floor",options=[1,2,3,4,5,6,7,],value=1)
year_built = st.number_input("Year Built", min_value=1800, max_value=2025, value=2000)
exterior = 1 if st.checkbox("Exterior") else 0
lift = 1 if st.checkbox("Lift") else 0
terrace = 1 if st.checkbox("Terrace") else 0
balcony = 1 if st.checkbox("Balcony") else 0
second_hand = st.selectbox("Second hand", [0, 1])
needs_renovating = st.selectbox("Need renovation?", [0, 1])
parking = st.selectbox("Parking", [0, 1])
swimming_pool = st.selectbox("Pool", [0, 1])
garden = st.selectbox("Garden", [0, 1])
air_conditioning = st.selectbox("Air Conditioning", [0, 1])
heating = st.selectbox("Heating", [0, 1])


city_name = st.selectbox("Choose the city:", list(city_map.keys()))
city_value = city_map[city_name]
price_cheap_neigh = st.number_input("Fator bairro vs mais barato", value=3.0)
price_cheap_property = st.number_input("Fator propriedade vs mais barata", value=2.0)


input_dict = {
    'city' : city_value,
    'sq_m_built': sq_m_built,
    'n_bedrooms': n_bedrooms,
    'bathrooms': bathrooms,
    'floor': floor,
    'year_built': year_built,
    'exterior': int(exterior),
    'lift': int(lift),
    'terrace': int(terrace),
    'balcony': int(balcony),
    'second_hand': int(second_hand),
    'needs_renovating': int(needs_renovating),
    'parking': int(parking),
    'swimming_pool': int(swimming_pool),
    'garden': int(garden),
    'air_conditioning': int(air_conditioning),
    'heating': int(heating),
    'price_cheap_city': city_value,
    'price_cheap_neigh': price_cheap_neigh,
    'price_cheap_property': price_cheap_property
}

input_df = pd.DataFrame([input_dict], columns=model_features)



if st.button("Estimate price"):
    input_scaled = scaler.transform(input_df)
    
    log_price = model.predict(input_scaled)[0]  # predição do log(preço)
    predicted_price = np.exp(log_price)         # desfazendo o log
    
    st.success(f"💶 Estimated property price: € {predicted_price:,.2f}")


df = pd.DataFrame(
    np.random.randn(1000, 2) / [2.1734] + [41.3851],
    columns=["lat", "lon"],
)
st.map(df)