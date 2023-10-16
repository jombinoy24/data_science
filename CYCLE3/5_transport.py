import matplotlib.pyplot as plt
print("******************************")
print("JOM BINOY")
print("--SJC22MCA-2033--")
print("--20MCA241--DATA SCIENCE LAB--")
print("--BATCH : 2022-2024--")
print("******************************")
# Data
transport_modes = ['Walking', 'cycling', 'car', 'Bus', 'train']
frequencies = [29, 15, 35, 18, 3]

# Create a bar graph
plt.bar(transport_modes, frequencies, width=0.1, color='green')

# Set labels and title
plt.xlabel('Mode of Transport')
plt.ylabel('Frequency')
plt.title('Primary Mode of Transport to School')

# Show the bar graph
plt.show()
