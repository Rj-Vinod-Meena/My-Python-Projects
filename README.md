# 🐍 Python Data Analysis & Logic Building Portfolio

Welcome to my project repository! Here, I have applied **Python, NumPy, Pandas, and Seaborn** to solve real-world data problems and build logical simulations.

---

## 📂 Project Details:
# 1. 📊 Stock Analyzer (Python)

This is a Python-based Stock Analysis Tool that fetches real-time financial data and generates:

* 📈 Financial Statements (P&L, Balance Sheet, Cash Flow)
* 📊 Key Ratios (P/E, ROE, Debt, etc.)
* 🤖 Basic AI-based Analysis (Pros & Cons)
* 📉 Interactive Stock Charts
* 📄 Excel Report Export

## 🚀 Features

* Automatic NSE ticker handling (.NS)
* Safe data fetching (error handling)
* Excel report with multiple sheets
* Interactive matplotlib charts with buttons

## 🛠️ Tech Stack

* Python
* yfinance API
* pandas
* matplotlib & seaborn

## ▶️ How to Run

```bash
pip install -r requirements.txt
python stock_analyzer.py
```

## 📌 Example Input

```
Enter Stock Name: TCS
```

## 📄 Output

* Excel report generated
* Interactive chart opens

## ⚠️ Note

* Internet connection required
* Data depends on Yahoo Finance API



# 2. 🛒 E-commerce Sales Analysis (`ecommerce_analysis.py`)
> **Tech Stack:** Python, Pandas, Seaborn, NumPy
- **Simulation:** Generated a dummy dataset of **100 orders** using NumPy.
- **Logic:** Calculated **Total Revenue** (Price × Quantity) for each order.
- **Analysis:** Grouped data by 'Product' to find the **Best-Selling Products**.
- **Visuals:** Created a Bar Chart using **Seaborn** to visualize product performance.

 # 3. 🏧 ATM Banking System (`ATM.py`)
> **Tech Stack:** Core Python (Loops & Conditions)
- **Logic Building:** A simulation of a real ATM machine.
- **Features:** Includes **PIN Authentication**, Balance Check, Withdrawal logic (with validation), and Deposit system.
- **Looping:** Uses `while` loops to keep the menu running until the user chooses to exit.

# 4. 📊 Student Exam Analysis (`marks_analysis.py`)
> **Tech Stack:** Python, NumPy
- **Matrix Operations:** Used 2D NumPy arrays to store marks of 5 students across 3 subjects.
- **Calculations:** Computed **Total Marks** (axis=1) and **Class Average**.
- **Filtering Logic:** Applied Boolean Masking to filter students who **Passed** (Total > 150).

# 5. 📈 Weekly Sales Report (`sales_analysis.py`)
> **Tech Stack:** Python, Pandas, Matplotlib
- **Data Handling:** Created a DataFrame to track daily sales and customer count.
- **Insights:** Calculated **Total Weekly Sales** and **Average Customer Footfall**.
- **Graphing:** Plotted a daily sales trend using Matplotlib.



---
*Created by Vinod Meena*
