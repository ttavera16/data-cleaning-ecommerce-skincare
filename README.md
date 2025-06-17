# Data Cleaning - Skincare E-commerce Dataset

This project focuses on cleaning a fictional skincare e-commerce dataset using Python. The dataset simulates real-world issues such as inconsistent formatting, missing values, and invalid data entries. The goal was to prepare the data for reliable use in analysis.

##  Project Objective

- Perform full data cleaning on a CSV file representing sales transactions from an online skincare store.
- Identify and correct inconsistencies in brand names, product names, and categories.
- Handle missing and invalid values, including negative prices and malformed dates.
- Export a clean version of the dataset to Excel for future use in dashboards or reports.

---

##  Tools Used

- **Python** (Pandas, NumPy)
- Excel (for final export)

---

##  Cleaning Steps

- Removed duplicate rows
- Trimmed special characters (`_`, `-`, `.`) and whitespace from text fields
- Normalized brand names to lowercase and corrected known inconsistencies
- Converted `order_date` to datetime format
- Replaced nulls in categorical columns with `"other"`
- Converted categorical fields to appropriate data types
- Set negative prices (where the item was not returned) to null
- Filled missing numeric values with the column median
- Exported cleaned data to `.xlsx`

---

##  Cleaned Dataset

The cleaned data includes the following key columns:

- `order_date`
- `product_name`
- `category`
- `brand`
- `price`
- `quantity`
- `return_flag`

Saved as:  
`ecommerce-data-cleaned.xlsx`

## 👩‍💻 Author

Treisi Tavera  
ttavera2002@gmail.com
www.linkedin.com/in/treisi-tavera
