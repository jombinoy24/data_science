print("******************************")
print("JOM BINOY")
print("--SJC22MCA-2033--")
print("--20MCA241--DATA SCIENCE LAB--")
print("--BATCH : 2022-2024--")
print("******************************")


def is_perfect_number(n):
  """Checks if a given number is a perfect number.

  Args:
    n: An integer.

  Returns:
    True if n is a perfect number, False otherwise.
  """

  sum_of_factors = 0
  for i in range(1, n):
    if n % i == 0:
      sum_of_factors += i
  return sum_of_factors == n


def main():
  n = int(input("Enter a number: "))
  if is_perfect_number(n):
    print(n, "is a perfect number.")
  else:
    print(n, "is not a perfect number.")


if __name__ == "__main__":
  main()
