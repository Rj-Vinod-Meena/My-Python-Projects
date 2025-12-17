import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Data Creation
data = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    'Sales': [1200, 1500, 1100, 1800, 2000, 2300, 2100],
    'Customers': [40, 50, 35, 60, 65, 80, 75]
}

# 2. Pandas DataFrame Creation (Table structure)
df = pd.DataFrame(data)

# 3. Data Visualization (Analysis)
print("--- Weekly Sales Report ---")
print(df)
print("\nTotal Sales:", df['Sales'].sum())
print("Average Customers:", df['Customers'].mean())

# 4. Graph Creation (Visualization)
plt.figure(figsize=(8, 5))
sns.barplot(x='Day', y='Sales', data=df, palette='viridis')
plt.title('Daily Sales Analysis')
plt.show() 