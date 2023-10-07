print("******************************")
print("JOM BINOY")
print("--SJC22MCA-2033--")
print("--20MCA241--DATA SCIENCE LAB--")
print("--BATCH : 2022-2024--")
print("******************************")
import cmath

def find_roots_of_quadratic_equation(a, b, c):
  """Returns the roots of the quadratic equation ax^2 + bx + c = 0.

  Args:
    a: The coefficient of the x^2 term.
    b: The coefficient of the x term.
    c: The constant term.

  Returns:
    A tuple of two complex numbers, representing the roots of the quadratic equation.
  """

  discriminant = b**2 - 4 * a * c
  if discriminant < 0:
    return (complex(-b / (2 * a), cmath.sqrt(-discriminant) / (2 * a)), complex(-b / (2 * a), -cmath.sqrt(-discriminant) / (2 * a)))
  elif discriminant == 0:
    return (-b / (2 * a), -b / (2 * a))
  else:
    return (-b + cmath.sqrt(discriminant)) / (2 * a), (-b - cmath.sqrt(discriminant)) / (2 * a)


def main():
  """Prints the roots of a quadratic equation, rounded to 2 decimal places."""

  a = float(input("Enter the coefficient of the x^2 term: "))
  b = float(input("Enter the coefficient of the x term: "))
  c = float(input("Enter the constant term: "))

  roots = find_roots_of_quadratic_equation(a, b, c)

  print("The roots of the quadratic equation are:")
  for root in roots:
    print(f"{round(root.real, 2)} + {round(root.imag, 2)}i")


if __name__ == "__main__":
  main()


