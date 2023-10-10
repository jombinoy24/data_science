print("******************************")
print("JOM BINOY")
print("--SJC22MCA-2033--")
print("--20MCA241--DATA SCIENCE LAB--")
print("--BATCH : 2022-2024--")
print("******************************")


def is_armstrong_number(num):
    # Convert the number to a string to count the number of digits
    num_str = str(num)
    num_digits = len(num_str)

    # Calculate the sum of the digits raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)

    # Check if it's an Armstrong number
    return armstrong_sum == num


# Loop through numbers from 1 to 1000 and check if they are Armstrong numbers
for i in range(1, 1001):
    if is_armstrong_number(i):
        print(i)
