print("******************************")
print("JOM BINOY")
print("--SJC22MCA-2033--")
print("--20MCA241--DATA SCIENCE LAB--")
print("--BATCH : 2022-2024--")
print("******************************")
def absent_digits(n):
    all_nums = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    n = set(n)  # Convert the input list to a set of integers
    n = n.symmetric_difference(all_nums)
    n = sorted(n)
    return n

# Use a list of integers as input
input_list = [9, 5, 2, 6, 0, 1, 4, 6, 8, 4]
print(absent_digits(input_list))
