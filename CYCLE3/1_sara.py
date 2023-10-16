import matplotlib.pyplot as plt
print("******************************")
print("JOM BINOY")
print("--SJC22MCA-2033--")
print("--20MCA241--DATA SCIENCE LAB--")
print("--BATCH : 2022-2024--")
print("******************************")
# Data
years = [2001, 2002, 2003, 2004, 2005, 2006, 2007]
car_values = [24000, 22500, 19700, 17500, 14500, 10000, 5800]

# Create a figure and subplot
fig, ax = plt.subplots()

# Set the style properties
ax.plot(years, car_values, color='red', linestyle='-.', marker='*', markersize=20, markerfacecolor='green')

# Set axis labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Car Value')
ax.set_title('Value Depreciation', loc='left')

# Show the plot
plt.show()
