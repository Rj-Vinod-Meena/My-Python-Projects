import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Data Generation (Using NumPy)
np.random.seed(5) 
products = ['Laptop', 'Mouse', 'Headphone', 'Keyboard', 'Monitor']

# 100 orders Data Creation
data = {
    'Product': np.random.choice(products, 100),  # Select Products Randomly 
    'Price': np.random.randint(500, 50000, 100), # Price b/w 500 to 50000
    'Quantity': np.random.randint(1, 10, 100)    # Quantity b/w 1 to 10
}

# 2. Data Handling (Using Pandas)
df = pd.DataFrame(data)

# Logic: Calculate Total Sales (Price * Quantity)
df['Total_Sales'] = df['Price'] * df['Quantity']

# Analysis: Total sales of each product?
product_performance = df.groupby('Product')['Total_Sales'].sum().reset_index()

# Sort to make the graph look good. (High to Low)
product_performance = product_performance.sort_values(by='Total_Sales', ascending=False)

# Printing the data to the console
print("--- Sales Data Preview (Top 5 Rows) ---")
print(df.head()) 
print("\n--- Product Wise Total Sales ---")
print(product_performance)

# 3. Data Visualization (Using Seaborn & Matplotlib)
plt.figure(figsize=(10, 6))

# Use the Barplot of Seaborn (It is prettier than mataplotlib)
sns.barplot(x='Product', y='Total_Sales', data=product_performance, palette='viridis')

# Details of Graph (Matplotlib features)
plt.title('Total Sales by Product Category', fontsize=16)
plt.xlabel('Product Name', fontsize=12)
plt.ylabel('Revenue (INR)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7) 

# Show Graph
print("\nShowing Graph...")
plt.show()