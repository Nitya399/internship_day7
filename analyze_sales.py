import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Connect to database (it will create if not exist)
conn = sqlite3.connect('sales_data.db')
cursor = conn.cursor()

# Step 2: Create sales table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT,
        quantity INTEGER,
        price REAL
    )
''')

# Step 3: Insert sample data
sample_data = [
    ('Product A', 10, 20.0),
    ('Product B', 15, 30.0),
    ('Product C', 5, 50.0),
    ('Product A', 7, 20.0),
    ('Product B', 12, 30.0),
    ('Product C', 8, 50.0),
]
cursor.executemany('INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)', sample_data)

# Commit the changes
conn.commit()

print("✅ Database, table created and sample data inserted successfully!")

# Step 4: Run SQL queries and Analyze
# Query 1: Total Quantity and Revenue per Product
query1 = '''
SELECT 
    product, 
    SUM(quantity) AS total_quantity, 
    SUM(quantity * price) AS total_revenue 
FROM 
    sales 
GROUP BY 
    product
'''
df1 = pd.read_sql_query(query1, conn)

# Query 2: Total Revenue Only
query2 = '''
SELECT 
    product, 
    SUM(quantity * price) AS revenue 
FROM 
    sales 
GROUP BY 
    product
'''
df2 = pd.read_sql_query(query2, conn)

# Query 3: Average Price per Product
query3 = '''
SELECT 
    product, 
    AVG(price) AS avg_price 
FROM 
    sales 
GROUP BY 
    product
'''
df3 = pd.read_sql_query(query3, conn)

# Step 5: Print Results
print("\n📈 Total Quantity and Revenue per Product:")
print(df1)

print("\n💰 Total Revenue per Product:")
print(df2)

print("\n🏷️ Average Price per Product:")
print(df3)

# Step 6: Plot Charts
fig, axs = plt.subplots(3, 1, figsize=(8, 18))

# Chart 1
axs[0].bar(df1['product'], df1['total_quantity'], color='skyblue')
axs[0].set_title('Total Quantity Sold per Product')
axs[0].set_ylabel('Quantity')

# Chart 2
axs[1].bar(df2['product'], df2['revenue'], color='lightgreen')
axs[1].set_title('Total Revenue per Product')
axs[1].set_ylabel('Revenue')

# Chart 3
axs[2].bar(df3['product'], df3['avg_price'], color='salmon')
axs[2].set_title('Average Price per Product')
axs[2].set_ylabel('Average Price')

plt.tight_layout()
plt.savefig("combined_sales_dashboard.png")
plt.show()

# Close the database connection
conn.close()

