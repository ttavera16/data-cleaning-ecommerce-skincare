# Author: Treisi Tavera
# Description: This script performs data cleaning on an e-commerce skincare dataset. It handles duplicates, 
# string formatting, missing values, and inconsistent text formatting. 
# The final cleaned dataset is exported as an Excel file for analysis or dashboarding.

import pandas as pd
import numpy as np
import openpyxl
import seaborn as sns
import matplotlib.pyplot as plt
# === Load dataset===

sales_data = pd.read_csv("ecommerce-sales.csv")

# Preview dataset shape and structure

print(sales_data.shape)
print(sales_data.head())
print(sales_data.info())

# === Remove duplicates ===
sales_data = sales_data.drop_duplicates()


# === Clean text fields: strip special characters and spaces ===
sales_data["product_name"] = sales_data["product_name"].str.strip("_-.")
sales_data["category"] = sales_data["category"].str.strip("_-.")
sales_data["brand"] = sales_data["brand"].str.strip("_-.")
sales_data["brand"] = sales_data["brand"].str.strip() 
sales_data["product_name"] = sales_data["product_name"].str.strip() 
sales_data["category"] = sales_data["category"].str.strip() 
sales_data["return_flag"] = sales_data["return_flag"].str.strip() #remueve cualquier espacio en el campo


# === Normalize return_flag values ===
sales_data["return_flag"] = sales_data["return_flag"].replace('y', 'yes')
sales_data["return_flag"] = sales_data["return_flag"].replace('n', 'no')



# === Convert order_date to datetime format ===

sales_data['order_date'] = pd.to_datetime(sales_data['order_date'], errors='coerce')



# === Normalize brand names: lowercase and remove symbols ===
sales_data['brand'] = sales_data['brand'].str.replace('-', '')
sales_data['brand'] = sales_data['brand'].str.replace('_', '')
sales_data['brand'] = sales_data["brand"].str.lower()


# === Fix known brand name inconsistencies ===

sales_data['brand'] = sales_data['brand'].replace({
    'glowrecipe': 'glow recipe',
    'theordinary': 'the ordinary',
    'larocheposay': 'la roche posay',
    'la rocheposay': 'la roche posay',
    'drunkelephant': 'drunk elephant',
    "paula'schoice": "paula's choice",
})


# === Handle missing values in categorical columns ===

sales_data['product_name'] = sales_data['product_name'].fillna('other') 
sales_data['category'] = sales_data['category'].fillna('other') 
sales_data['return_flag'] = sales_data['return_flag'].fillna('other') 
sales_data['brand'] = sales_data['brand'].fillna('other') 

# Convert to categorical types
sales_data['product_name'] = sales_data['product_name'].astype('category')
sales_data['category'] = sales_data['category'].astype('category')
sales_data['brand'] = sales_data['brand'].astype('category')
sales_data['return_flag'] = sales_data['return_flag'].astype('category')



# === Handle negative prices ===
# If price is negative and not a returned item, set it to NaN
sales_data['price'] = np.where((sales_data['price'] < 0) & (sales_data['return_flag'] != 'yes'), 
    np.nan, sales_data['price'])

# === Fill missing numeric values (price) with the median ===
sales_data['price'] = sales_data['price'].fillna(sales_data['price'].median())


# === Export cleaned data ===

sales_data.to_excel("ecommerce-data-cleaned.xlsx", index=False)





