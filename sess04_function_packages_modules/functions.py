# This file demonstrates defining & calling/invoking user-defined functions in Python
from sess02_python_data_types.python_arithmetic_operations import difference


# -------------------------------------------
# 1. Define a simple function with no params
# -------------------------------------------
def greeting():
    """Prints a hello message."""
    print("Hello from 'greeting()' function")


# call the greeting function
greeting()


# -------------------------------------------
# 2. Define a function that accepts a parameter
# -------------------------------------------
def greet_user(username):
    """Greets a user by name."""
    print("Hello %s from python function" % username)


# prompt user
name = input("Please enter your name: \n")
greet_user(name)


# -----------------------------------------------------------
# 3. Function that adds or multiplies two numbers
# -----------------------------------------------------------
def add_or_multiply(first_num, second_num, operator='+'):
    """
    Returns addition or multiplication based on operator.
    operator: '+' or '*'
    """
    if operator == '+':
        return first_num + second_num
    elif operator == '*':
        return first_num * second_num
    else:
        return f"Invalid operator '{operator}' given.\nPlease use '+' or '*'"


# call the function
print(f"The sum of 3 and 5 is: {add_or_multiply(3, 5, '+')}")
print(f"The product of 3 and 5 is: {add_or_multiply(3, 5, '*')}")


# print documentation for add_or_multiply correctly
print(f"\nThe documentation for the add_or_multiply function is:\n{add_or_multiply.__doc__}")


# ----------------------------------------------------------
# 4. Anonymous / lambda functions
# ----------------------------------------------------------
plus_five = lambda num: num + 5
print(f"The sum of 7 and 5 using a lambda function is: {plus_five(7)}")


def add_five(num):
    """Adds 5 to a number."""
    return num + 5


print(f"The sum of 5 and 7 is: {add_five(5)}")


# lambda for difference
difference = lambda num1, num2: num1 - num2
print(f"The difference between 3 and 5 using lambda is: {difference(3, 5)}")


# ----------------------------------------------------------
# 5. Function with variable number of parameters
# ----------------------------------------------------------
def get_sum(*values):
    """
    Returns the sum of all values passed in.

    Example:
    >>> get_sum(1,2,3)
    6
    >>> get_sum(3.5,2.1,1.4)
    7.0
    >>> get_sum(1,2,"3")
    TypeError
    """
    try:
        return sum(values)
    except TypeError as e:
        raise TypeError("All the values provided must be numbers/numeric") from e


# lists for testing
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"The sum of the first ten numbers is: {get_sum(*num_list)}")

nums_with_decimals = [4.5, 1.5, 2.0]
print(f"The sum of 4.5, 1.5 and 2.0 is: {get_sum(*nums_with_decimals)}")

# ❌ FIXED: missing comma between 5 and "7"
mixed_nums = [2, 5, "7"]
print("\nThe next line will produce an ERROR because of a string in the list:")
try:
    print(get_sum(*mixed_nums))
except Exception as e:
    print(e)


# ----------------------------------------------------------
# 6. Entry point
# ----------------------------------------------------------
if __name__ == "__main__":
    print("\nRunning inside __main__ block...\n")

    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"The sum of the first ten numbers is: {get_sum(*num_list)}")

    nums_with_decimals = [4.5, 1.5, 2.0]
    print(f"The sum of 4.5, 1.5 and 2.0 is: {get_sum(*nums_with_decimals)}")

    mixed_nums = [2, 5, "7"]
    try:
        print(f"The sum of 2, 5 and 7 is: {get_sum(*mixed_nums)}")
    except Exception as e:
        print(e)
