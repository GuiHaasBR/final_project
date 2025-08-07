# Final Project

## Introduction

An analisys about real real state data from the city of Barcleona, Spain. 
This project have the objetive to analize how differents indicators can influence on the price of the properties. 


- 🛠 GitHub Repository: [final_project](https://github.com/GuiHaasBR/final_project)
- 📋 Trello Board: [Project Tasks & Timeline](https://trello.com/b/tKmaOyHQ/barcelona-real-state) 
- Presentation: 

## Datasets Used

 *  **Idealista Data Exploration: Barcelona Real Estate:** Web Scraping, Data Cleaning and Exploratory Data Analysis.

At the same time, we were provided with a Metadata(dictionary) to help us understand the content of the columns in each file and guide us through the analysis

* **id:** Property identificator.
* **property_type:** Type of property.
* **adress:** Approximated adress of property.
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
* **central_heating:** Is the heating system cental/individual?
* **heating_type:** Type of heating.
* **consumption_in_mkw/m2_year:** Yearly consumtion of the property in mkW/m^2.
* **emissions_in_kgco2/m2_year:** Yearly emissions of the property in kgco2/m^2.
* **orientation:** Orientation of the property.
* **description:** Text description of the property.

**Comments on the Data:**

* **Main Challenges:** 
* **Strengths:** 
* **Weaknesses:** 

##  Business Problem & Hypothesis
Create Machine Learning model to predict stroke based on patient's symtoms

* **Question:** 
* **Conclusion:**  

_*Business recommendation*_: 

## Methodology

Our methodology involved several key steps, focusing on data preprocessing, ML-Model selection, Model training , Model evaluation, and tuning

1.  **Data preprocessing:** 
    * Datasets were downloaded from kaggle.
    * Data Cleaning: 
        * maping categorical values to numerical, drop "id" column, not considering gender "Other"
        * fillna bmi with average value
2.  **Model selection:** 
3.  **Model training:**  

4.  **Model evaluation:** 

5.  **Model tuning:**

6.  **Insights:**

  **Data Analysis Tools and Libraries:**
* __Python__: The primary programming language for data manipulation and analysis.
* __Pandas__:Essential for data loading, cleaning, and transformation.
* __Matplotlib / Seaborn__: Used for creating various visualizations (bar charts, line graphs).

##  Repository Structure

```
proj-vanguard-abtest/
├── data/                        # Raw and cleaned CSV files
├── figures/                     # Sketching of structure in dataset
├── notebooks/                   # Python notebooks with analysis
├── README.md                    # This file
└── slides                       # Url of presentation
```
## 👥 Project by:
__*Guilherme Haas*__