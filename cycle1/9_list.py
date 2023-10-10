print("******************************")
print("JOM BINOY")
print("--SJC22MCA-2033--")
print("--20MCA241--DATA SCIENCE LAB--")
print("--BATCH : 2022-2024--")
print("******************************")
# Initialize the Python lists
lt1 = [5, 10, 15, 20, 25, 30]
lt2 = [2, 4, 6, 8, 10, 12]

# Print the original list elements
print("Python Original list 1: " + str(lt1))
print("Python Original list 2: " + str(lt2))

# Use a naive method to add two lists.
res_lt = []  # Declaration of the list
for x in range(0, len(lt1)):
    res_lt.append(lt1[x] + lt2[x])

# Display the sum of two lists in Python
print("Addition of the list lt1 and lt2 is: " + str(res_lt))
