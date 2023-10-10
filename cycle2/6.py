print("******************************")
print("JOM BINOY")
print("--SJC22MCA-2033--")
print("--20MCA241--DATA SCIENCE LAB--")
print("--BATCH : 2022-2024--")
print("******************************")
import numpy as np

array_2d = np.array([[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9, 10, 11, 12],
                     [13, 14, 15, 16]])

a_result = array_2d[1:, :]


b_result = array_2d[:, :-1]


c_result = array_2d[1:3, 0:2]

d_result = array_2d[:, 1:3]


e_result = array_2d[0, 1:3]


f_result = array_2d[1:].flatten()[::-1]

print("a. Display all elements excluding the first row:")
print(a_result)

print("\nb. Display all elements excluding the last column:")
print(b_result)

print("\nc. Display the elements of the 1st and 2nd column in the 2nd and 3rd row:")
print(c_result)

print("\nd. Display the elements of the 2nd and 3rd column:")
print(d_result)

print("\ne. Display the 2nd and 3rd element of the 1st row:")
print(e_result)

print("\nf. Display the elements from indices 4 to 10 in descending order:")
print(f_result)
