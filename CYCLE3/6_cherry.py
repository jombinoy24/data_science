import matplotlib.pyplot as plt
print("******************************")
print("JOM BINOY")
print("--SJC22MCA-2033--")
print("--20MCA241--DATA SCIENCE LAB--")
print("--BATCH : 2022-2024--")
print("******************************")
# Height data
heights = [61, 63, 64, 66, 68, 69, 71, 71.5, 72, 72.5, 73, 73.5, 74, 74.5, 76, 76.2, 76.5, 77, 77.5, 78, 78.5, 79, 79.2, 80, 81, 82, 83, 84, 85, 87]

# Create a histogram with a bin size of 5
plt.hist(heights, bins=range(60, 90, 5), edgecolor='black')

# Set labels and title
plt.xlabel('Height (in inches)')
plt.ylabel('Frequency')
plt.title('Cherry Tree Heights Histogram')

# Show the histogram
plt.show()
