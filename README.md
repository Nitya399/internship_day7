# 📊 Sales Data Analysis with Python and SQLite

This repository presents a simple Sales Data Analysis project demonstrating the use of Python, SQLite, SQL queries, and basic data visualization.

---

## 📁 Dataset Information

We created a synthetic sales dataset stored inside a SQLite database (`sales_data.db`) with the following structure:

- `id`: Unique identifier (Primary Key)
- `product`: Name of the product
- `quantity`: Number of units sold
- `price`: Price per unit of the product

The dataset includes sales records for multiple products with varying quantities and prices.

---

## 🎯 Project Objectives

- Create and populate a small sales database using SQLite and Python
- Write and execute SQL queries to analyze sales performance
- Load SQL query results into Pandas DataFrames
- Visualize the analysis results using bar charts
- Combine SQL + Python + Data Visualization into one workflow

---

## 🛠 Tools and Libraries Used

- Python 3.x
- SQLite3 (Python's built-in library)
- Pandas
- Matplotlib

---

## 📊 SQL Queries and Visualizations

We performed the following analyses:

- **Total Quantity Sold per Product**
  - SQL:  
    ```sql
    SELECT product, SUM(quantity) AS total_quantity FROM sales GROUP BY product;
    ```
  - 📈 Bar chart showing total quantity sold for each product.

- **Total Revenue per Product**
  - SQL:  
    ```sql
    SELECT product, SUM(quantity * price) AS total_revenue FROM sales GROUP BY product;
    ```
  - 📈 Bar chart showing total revenue generated per product.

- **Average Price per Product**
  - SQL:  
    ```sql
    SELECT product, AVG(price) AS avg_price FROM sales GROUP BY product;
    ```
  - 📈 Bar chart showing average price per product.

---

## 📂 Project Structure

```plaintext
├── create_sales.py         # Script to create the sales_data.db and insert sample sales records
├── analyze_sales.py        # Script to query the database, print results, and visualize data
├── sales_data.db           # Generated SQLite database file
├── README.md               # Project documentation (this file)
```

---

## ⚙️ How to Run the Project

1. **Create the database:**
   ```bash
   python create_sales.py
   ```

2. **Analyze and visualize the sales data:**
   ```bash
   python analyze_sales.py
   ```

This will:
- Execute SQL queries
- Print analysis results
- Generate three bar charts based on the queries

---

## 📌 Key Insights

- **Product B** generated the highest total revenue.
- **Product A** had the highest quantity sold.
- **Product C** had the highest average price.
- Visualizations helped quickly identify sales trends and product performance.

---

## 🚀 Future Improvements

- Add timestamps for time-series analysis (e.g., monthly or quarterly sales trends)
- Expand dataset to include customer data, regions, and categories
- Save visualizations automatically to image files
- Build a basic interactive dashboard using Streamlit or Dash
- Automate database updates from CSV files

---

## 📞 Contact

Feel free to connect for any suggestions, improvements, or collaboration ideas related to this project! 🚀

---

# 🎯 Conclusion

This project provides a hands-on demonstration of working with databases, performing data analysis with SQL, and visualizing business insights using Python.  
It showcases how quickly simple business intelligence can be achieved with lightweight tools!

---
