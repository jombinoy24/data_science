# Import necessary libraries
import pandas as pd
from sklearn.datasets import make_classification

# Generate synthetic data for demonstration
X, y = make_classification(
    n_samples=1000, n_features=5, n_informative=3, n_redundant=1,
    n_classes=3, random_state=42
)

# Create a DataFrame with car details and labels
df = pd.DataFrame(X, columns=['Feature1', 'Feature2', 'Feature3', 'Feature4', 'Feature5'])
df['Label'] = y

# Save the DataFrame to a CSV file
df.to_csv('car_details.csv', index=False)

# Display the first few rows of the DataFrame
print(df.head())
