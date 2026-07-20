# Pandas Basics

# Pandas is the most popular library for data manipulation and analysis in Python.
# It provides two main data structures: Series (1D) and DataFrame (2D).

import pandas as pd
import numpy as np

print("=== Pandas Basics - Enhanced Guide ===\n")
print(f"Pandas Version: {pd.__version__}\n")

# 1. Creating DataFrames
print("=== 1. Creating DataFrames ===")

# From dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'London', 'Paris', 'Tokyo'],
    'Salary': [70000, 80000, 65000, 90000]
}
df = pd.DataFrame(data)
print("DataFrame from dict:\n", df)

# From list of lists
df2 = pd.DataFrame([
    ['Eve', 24, 'Berlin', 72000],
    ['Frank', 32, 'Madrid', 85000]
], columns=['Name', 'Age', 'City', 'Salary'])
print("\nDataFrame from list:\n", df2)

# 2. Basic DataFrame Operations
print("\n=== 2. Basic Inspection ===")
print("Shape          :", df.shape)
print("Columns        :", df.columns.tolist())
print("Data Types     :\n", df.dtypes)
print("First 2 rows   :\n", df.head(2))
print("Last 2 rows    :\n", df.tail(2))
print("Info summary   :")
df.info()

# 3. Selecting Data
print("\n=== 3. Selecting Data ===")
print("Single Column (Name):\n", df['Name'])
print("Multiple Columns:\n", df[['Name', 'City']])

# loc (label-based) and iloc (position-based)
print("loc[0:2] (rows 0-2):\n", df.loc[0:2, ['Name', 'Age']])
print("iloc[0:2] (first 2 rows):\n", df.iloc[0:2])

# Filtering
print("People older than 28:\n", df[df['Age'] > 28])

# 4. Summary Statistics
print("\n=== 4. Summary Statistics ===")
print(df.describe())                    # Numeric summary
print("\nValue counts for City:\n", df['City'].value_counts())

# 5. Data Manipulation
print("\n=== 5. Data Manipulation ===")

# Adding a new column
df['Senior'] = df['Age'] >= 30
print("Added 'Senior' column:\n", df)

# Sorting
print("Sorted by Salary:\n", df.sort_values(by='Salary', ascending=False))

# GroupBy
print("\nAverage Salary by City:")
print(df.groupby('City')['Salary'].mean())

# 6. Handling Missing Data
print("\n=== 6. Handling Missing Data ===")
df_with_nan = df.copy()
df_with_nan.loc[1, 'Salary'] = np.nan
print("With NaN:\n", df_with_nan)
print("Filled NaN with mean:\n", df_with_nan.fillna(df_with_nan['Salary'].mean()))

# 7. Reading & Writing Data
print("\n=== 7. Reading & Writing ===")
# Save to CSV
df.to_csv('employees.csv', index=False)
print("Saved to 'employees.csv'")

# Read CSV
df_read = pd.read_csv('employees.csv')
print("Read from CSV:\n", df_read.head())

print("\n=== Pandas is the go-to tool for data analysis in Python! ===")
print("Next: Learn Data Cleaning, Merging, Visualization with Matplotlib/Seaborn.")