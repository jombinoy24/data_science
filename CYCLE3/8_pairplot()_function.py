import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# Load the iris dataset (if not already loaded)
iris_data = pd.read_csv('iris.csv')  # Replace with the actual dataset path

# Define different kinds of plots and markers
kinds = ['scatter', 'kde', 'hist', 'reg']
markers = ['.', 's', '+', 'd']

# Create pairplots for each combination of kinds and markers
for kind in kinds:
    for marker in markers:
        sns.set(style="whitegrid")
        g = sns.pairplot(iris_data, hue="variety", kind=kind, markers=marker)
        plt.title(f"Pairplot with kind='{kind}' and marker='{marker}'")
        plt.show()
