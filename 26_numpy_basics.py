# NumPy Basics

# NumPy is the fundamental package for scientific computing in Python.
# It provides support for large, multi-dimensional arrays and matrices,
# along with a large collection of high-level mathematical functions.

import numpy as np

print("=== NumPy Basics - Enhanced Guide ===\n")
print(f"NumPy Version: {np.__version__}\n")

# 1. Creating Arrays
print("=== 1. Creating Arrays ===")

# From lists
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)

# Special arrays
print("Zeros (3x3):")
print(np.zeros((3, 3)))

print("Ones (2x4):")
print(np.ones((2, 4)))

print("Identity matrix (3x3):")
print(np.eye(3))

print("Random values (2x3):")
print(np.random.rand(2, 3))

# Using arange and linspace
print("arange(0, 10, 2):", np.arange(0, 10, 2))
print("linspace(0, 1, 5) :", np.linspace(0, 1, 5))

# 2. Array Attributes
print("\n=== 2. Array Attributes ===")
a = np.array([[1, 2, 3], [4, 5, 6]])
print("Shape      :", a.shape)
print("Dimension  :", a.ndim)
print("Data Type  :", a.dtype)
print("Size       :", a.size)
print("Item Size  :", a.itemsize, "bytes")

# 3. Basic Operations
print("\n=== 3. Arithmetic Operations ===")
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print("Addition    :", x + y)
print("Multiplication:", x * y)
print("Division    :", y / x)
print("Exponent    :", x ** 2)

# Broadcasting
print("Broadcasting example:")
print(np.array([1, 2, 3]) + 10)

# 4. Indexing & Slicing
print("\n=== 4. Indexing & Slicing ===")
matrix = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("Original:\n", matrix)

print("Element [1,2] :", matrix[1, 2])
print("First row     :", matrix[0])
print("Last column   :", matrix[:, -1])
print("Submatrix     :\n", matrix[0:2, 1:3])

# 5. Statistical Operations
print("\n=== 5. Statistical Operations ===")
data = np.array([2, 4, 4, 5, 6, 8, 9, 10])

print("Mean       :", data.mean())
print("Median     :", np.median(data))
print("Std Dev    :", data.std())
print("Min/Max    :", data.min(), data.max())
print("Sum        :", data.sum())

# 6. Reshaping & Transposing
print("\n=== 6. Reshaping ===")
arr = np.arange(12)
print("Original     :", arr)
print("Reshaped 3x4 :\n", arr.reshape(3, 4))
print("Flattened    :", arr.ravel())

# 7. Boolean Indexing & Filtering
print("\n=== 7. Boolean Indexing ===")
ages = np.array([15, 22, 18, 35, 16, 28])
adults = ages[ages >= 18]
print("Ages >= 18:", adults)

# 8. Why Use NumPy?
print("\n=== Why NumPy? ===")
print("""
- Fast vectorized operations (much faster than pure Python lists)
- Memory efficient
- Foundation for Pandas, SciPy, Matplotlib, Scikit-learn
- Broadcasting, linear algebra, random number generation
""")

print("\n=== NumPy is the backbone of Data Science & Scientific Computing in Python! ===")
print("Next steps: Learn Pandas for data analysis.")