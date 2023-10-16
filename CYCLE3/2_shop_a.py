import matplotlib.pyplot as plt
print("******************************")
print("JOM BINOY")
print("--SJC22MCA-2033--")
print("--20MCA241--DATA SCIENCE LAB--")
print("--BATCH : 2022-2024--")
print("******************************")
# Data
days = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri']
drinks_sales = [300, 450, 150, 400, 650]
food_sales = [400, 500, 350, 300, 500]

# Create a figure and two subplots in two rows
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 8))

# Plot for Drinks
ax1.plot(days, drinks_sales, linestyle='dotted', color='cyan', marker='H', markersize=8, markerfacecolor='magenta', markeredgecolor='black')
ax1.set_xlabel('Days of week')
ax1.set_ylabel('Sale of Drinks')
ax1.set_title('Sales Data1', loc='right')

# Plot for Food
ax2.plot(days, food_sales, linestyle='dotted', color='cyan', marker='H', markersize=8, markerfacecolor='magenta', markeredgecolor='black')
ax2.set_xlabel('Days of week')
ax2.set_ylabel('Sale of Food')
ax2.set_title('Sales Data2', loc='right')

# Add a grid with blue color
ax1.grid(color='blue')
ax2.grid(color='blue')

# Adjust spacing between subplots
plt.tight_layout()

# Show the plots
plt.show()
#---------------------b part-----------------


