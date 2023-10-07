print("******************************")
print("JOM BINOY")
print("--SJC22MCA-2033--")
print("--20MCA241--DATA SCIENCE LAB--")
print("--BATCH : 2022-2024--")
print("******************************")
def triangle_type(a, b, c):
  """Returns the type of triangle, given the lengths of its sides.

  Args:
    a: The length of the first side.
    b: The length of the second side.
    c: The length of the third side.

  Returns:
    A string representing the type of triangle, which can be "equilateral",
    "isosceles", or "scalene".
  """

  if a == b == c:
    return "equilateral"
  elif a == b or b == c or c == a:
    return "isosceles"
  else:
    return "scalene"


# Driver code
a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))


triangle_type = triangle_type(a, b, c)

print("The triangle is of type", triangle_type)
