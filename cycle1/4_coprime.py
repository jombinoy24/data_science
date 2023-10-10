print("******************************")
print("JOM BINOY")
print("--SJC22MCA-2033--")
print("--20MCA241--DATA SCIENCE LAB--")
print("--BATCH : 2022-2024--")
print("******************************")
def is_coprime(a, b):
  """Returns True if the given pair of numbers is coprime, False otherwise.

  Args:
    a: The first number.
    b: The second number.

  Returns:
    A boolean value indicating whether the given pair of numbers is coprime.
  """

  gcd = 1
  for i in range(2, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
      gcd = i
  return gcd == 1


# Driver code
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if is_coprime(a, b):
  print("The given pair of numbers is coprime.")
else:
  print("The given pair of numbers is not coprime.")
