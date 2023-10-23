# Task 2 - Program 2
# Python Program Create a Function with a Parameter which can do x^y

def power(x, y):
    """
  This function returns the power of x to y.

  Args:
    x: The base number.
    y: The exponent.

  Returns:
    The power of x to y.
  """

    if y == 0:
        return 1
    elif y == 1:
        return x
    else:
        return x * power(x, y - 1)


X = int(input("Enter the Value of X : \n"))
Y = int(input("Enter the Value of Y : \n"))
print(pow(X, Y))
