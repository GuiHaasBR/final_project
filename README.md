# Final Project

# Real Estate Price Estimator in Barcelona

## Introduction

An analisys about real real state data from the city of Barcelona, Spain. 
This project have the objetive to analize how differents indicators can influence on the price of the properties. 

This project involves an analysis of real estate data from the city of Barcelona, Spain. The main objective is to explore how different property features and indicators influence the price of properties in the city and to create a Machine Learning model capable of estimating property prices.


- 🛠 GitHub Repository: [final_project](https://github.com/GuiHaasBR/final_project)
- 📋 Trello Board: [Project Tasks & Timeline](https://trello.com/b/tKmaOyHQ/barcelona-real-state) 
- Presentation: 

# Project Overview

## Datasets Used

 *  **Idealista Data Exploration: Barcelona Real Estate:** Web Scraping, Data Cleaning, and Exploratory Data Analysis.

The dataset contains information such as:


* **id:** Property identifier.
* **property_type:** Type of property.
* **adress:** Approximate address of property.
* **neighborhood:** Neighborhood name.
* **city:** City name.
* **price:** Price in euros.
* **sq_mt_built:**: Area of the property in square meters with walls.
* **sq_mt_floor_area:** Usable area of the property in square meters.
* **n_bedrooms:** Bedrooms amount.
* **bathrooms:** Bathrooms amount.
* **floor_y:** Floor number.
* **year_built:** Year of building construction.
* **exterior_x:** Is the property exterior? (True/False).
* **lift_x:** Has the property a lift? (True/False).
* **terrace:** Has the property a terrace? (True/False).
* **balcony:** Has the property a balcony? (True/False).
* **second hand:** Is the property second hand? (True/False).
* **needs renovating:** Does the property need renovating? (True/False).
* **parking:** Has the property a parking slot? (True/False).
* **swimming pool:** Has the property a swimming pool? (True/False).
* **garden:**  Has the property a garden? (True/False).
* **air conditioning:** Has the property air conditioning? (True/False).
* **heating:** Has the property a heating system? (True/False).
* **central_heating:** Is the heating system central/individual?
* **heating_type:** Type of heating.
* **consumption_in_mkw/m2_year:** Yearly consumption of the property in mkW/m^2.
* **emissions_in_kgco2/m2_year:** Yearly emissions of the property in kgco2/m^2.
* **orientation:** Orientation of the property.
* **description:** Text description of the property.

##  Business Problem & Hypothesis

Create Machine Learning model to predict prices based on characteristics of properties.

* **Problem:** To accurately estimate the market price of properties in Barcelona using property characteristics.
* **Hypothesis:** Property features such as location, size, number of bedrooms, and amenities significantly affect the price.

## Methodology

The methodology involved several key steps, focusing on data preprocessing, ML-Model selection, Model training , Model evaluation, and tuning.

1.  **Data Collection:**
       * Datasets were downloaded from Kaggle.

2.  **Data Cleaning:** 
       * Handling missing values, encoding categorical variables, and filtering outliers.
          
3.  **Exploratory Data Analysis:**
       * Visualizing distributions, correlations, and patterns.
    
4.  **Modeling:**
       * Training various regression models and selecting the best based on error metrics.
  
5.  **Evaluation:**
       * Using metrics like RMSE and MAE to evaluate model performance.

6.  **Deployment:**
       * Developing a Streamlit app for interactive price estimation and neighborhood comparison.

7.  **Insights**


## Results & Insights

> Model provides accurate price predictions with acceptable error margins.

> Neighborhood and number of bedrooms are among the most influential factors.

> Properties with amenities like parking, terrace, and pool tend to have higher prices.

> Visualization tools help users compare prices across neighborhoods with similar features.


## How to Use the App

Input property features such as size, bedrooms, bathrooms, amenities, city, and neighborhood.

The app predicts the estimated market price.

Compare your property’s price with similar properties in nearby neighborhoods.


## Data Analysis Tools and Libraries:

* __Python__: The primary programming language for data manipulation and analysis.
* __Pandas__:Essential for data loading, cleaning, and transformation.
* __Matplotlib / Seaborn__: Used for creating various visualizations (bar charts, line graphs).
* __StreamLit__ : Create app. 

##  Repository Structure

```
proj-vanguard-abtest/
├── data/                        # Raw and cleaned CSV files
├── figures/                     # Sketching of structure in dataset
├── models/                      # ML models
├── notebooks/                   # Python notebooks with analysis
├── pipelines/                   # ML pipelines
├── scalers/                     # ML scalers
├── app.py                       # Executor of the App
├── README.md                    # This file
└── slides                       # URL of presentation
```
## 👥 Project by:
__*Guilherme Haas*__