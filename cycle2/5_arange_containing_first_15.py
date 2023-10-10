print("******************************")
print("JOM BINOY")
print("--SJC22MCA-2033--")
print("--20MCA241--DATA SCIENCE LAB--")
print("--BATCH : 2022-2024--")
print("******************************")
import numpy as np
even_numbers = np.arange(2, 31, 2)
a_result = even_numbers[2:9:2]
a_result_slice = even_numbers[2:9:2]
b_result = even_numbers[-3:]
c_result = even_numbers[::2]
d_result = even_numbers[-4:-1:2]
print("a. Elements from index 2 to 8 with step 2:", a_result)
print("a. Elements from index 2 to 8 with step 2 (using slice):", a_result_slice)
print("b. Last 3 elements of the array using negative index:", b_result)
print("c. Alternate elements of the array:", c_result)
print("d. Display the last 3 alternate elements:", d_result)
