import streamlit as st
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Carregar modelo e dados
with open(r"C:\Users\User\Desktop\IronHack\Week_8\Day1\final_project\models\model_ada_1M.pkl", "rb") as file:
    model = joblib.load(file)

df = pd.read_csv(r"C:\Users\User\Desktop\IronHack\Week_8\Day1\final_project\data\clean\df_1M.csv")

neighborhood_list = sorted(df['neighborhood'].unique())
city_list = sorted(df['city'].unique())
property_list = sorted(df['property_type'].unique())

model_features = ['property_type','neighborhood','city','sq_m_built', 'n_bedrooms', 'bathrooms', 'floor', 'year_built',
                  'exterior', 'lift', 'terrace', 'balcony','parking', 'swimming_pool', 'garden',
                  'air_conditioning', 'heating', 'price_cheap_city',
                  'price_cheap_neigh', 'price_cheap_property']

st.title("🏘️ Barcelona Price Estimator")

sq_m_built = st.number_input("Size in m²", min_value=20, max_value=1000, value=80)
n_bedrooms = st.number_input("Bedrooms", min_value=0, max_value=10, value=2)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=5, value=1)
floor = st.select_slider("Floor", options=list(range(1, 16)), value=1)
year_built = st.number_input("Year Built", min_value=1800, max_value=2025, value=2000)
exterior = 1 if st.checkbox("Exterior") else 0
lift = 1 if st.checkbox("Lift") else 0
terrace = 1 if st.checkbox("Terrace") else 0
balcony = 1 if st.checkbox("Balcony") else 0
parking = 1 if st.checkbox("Parking") else 0
swimming_pool = 1 if st.checkbox("Pool") else 0
garden = 1 if st.checkbox("Garden") else 0
air_conditioning = 1 if st.checkbox("Air Conditioning") else 0
heating = 1 if st.checkbox("Heating") else 0

city = st.selectbox("Choose the city:", city_list)
filtered_neighborhoods = sorted(df[df['city'] == city]['neighborhood'].unique())
neighborhood = st.selectbox("Choose the neighborhood:", filtered_neighborhoods)
property_type = st.selectbox("Choose the property type:", property_list)

price_cheap_neigh_map = dict(zip(df['neighborhood'], df['price_cheap_neigh']))
price_cheap_city_map = dict(zip(df['city'], df['price_cheap_city']))
price_cheap_property_map = dict(zip(df['property_type'], df['price_cheap_property']))

price_cheap_neigh = price_cheap_neigh_map.get(neighborhood, 0)
price_cheap_city = price_cheap_city_map.get(city, 0)
price_cheap_property = price_cheap_property_map.get(property_type, 0)

input_dict = {
    'property_type': property_type,        
    'neighborhood': neighborhood,        
    'city': city,                         
    'sq_m_built': sq_m_built,
    'n_bedrooms': n_bedrooms,
    'bathrooms': bathrooms,
    'floor': floor,
    'year_built': year_built,
    'exterior': exterior,
    'lift': lift,
    'terrace': terrace,
    'balcony': balcony,
    'parking': parking,
    'swimming_pool': swimming_pool,
    'garden': garden,
    'air_conditioning': air_conditioning,
    'heating': heating,
    'price_cheap_city': price_cheap_city,
    'price_cheap_neigh': price_cheap_neigh,
    'price_cheap_property': price_cheap_property
}

input_df = pd.DataFrame([input_dict], columns=model_features)

if st.button("Estimate price"):
    log_price = model.predict(input_df)[0]
    predicted_price = np.exp(log_price)
    st.success(f"💶 Estimated property price: € {predicted_price:,.2f}")

    

st.subheader(f"📊 Comparison of average price per neighborhood in {city} for properties with {n_bedrooms} bedrooms")

df_city = df[df['city'] == city]

bedroom_min = max(0, n_bedrooms - 1)
bedroom_max = n_bedrooms + 1

df_filtered = df_city[(df_city['n_bedrooms'] >= bedroom_min) & (df_city['n_bedrooms'] <= bedroom_max)]

top_neigh_filtered = (
    df_filtered[df_filtered['neighborhood'] != neighborhood]
    .groupby('neighborhood')
    .size()
    .sort_values(ascending=False)
    .head(4)
    .index
    .tolist()
)

compare_neighs = [neighborhood] + top_neigh_filtered

df_compare = df_filtered[df_filtered['neighborhood'].isin(compare_neighs)]

price_by_neigh = (
    df_compare.groupby('neighborhood')['price']
    .mean()
    .reset_index()
    .sort_values(by='price', ascending=False)
)

fig, ax = plt.subplots(figsize=(10,6))
sns.barplot(data=price_by_neigh, x='neighborhood', y='price', ax=ax, palette='coolwarm')

ax.set_xlabel("Neighborhood")
ax.set_ylabel("Average Price (€)")
ax.set_title(f"Average price per neighborhood in {city} for properties with {n_bedrooms} bedrooms")
plt.xticks(rotation=45)

st.pyplot(fig)
