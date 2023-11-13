import pandas as pd

# Step 1: Read the 'iris' dataset using read_csv()
iris_data = pd.read_csv('iris.csv')  # Replace 'iris.csv' with the actual file path

# i) Display Shape of the data set
print("i) Shape of the data set:")
print(iris_data.shape)
print()

# ii) First 5 and last 5 rows of the data set (head and tail)
print("ii) First 5 rows of the data set:")
print(iris_data.head())
print()

print("Last 5 rows of the data set:")
print(iris_data.tail())
print()

# iii) Size of the dataset
print("iii) Size of the dataset:")
print(iris_data.size)
print()

# iv) Number of samples available for each variety
print("iv) Number of samples available for each variety:")
print(iris_data['variety'].value_counts())
print()

# v) Description of the data set (use describe)
print("v) Description of the data set:")
print(iris_data.describe())
