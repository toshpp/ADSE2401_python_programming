# python script to demonstrate function decorators

# Function to get nth Fibonacci number using recursion
def fibonacci(n):
    """
    Calculates the n-th Fibonacci number using recursion.

    :param n:(int): The n-th Fibonacci number.

    :return: The n-th Fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#fibonacci() function decorator
def fibonacci_decorator(func):
    """
    Decorator function that adds a print() statement before and after executing the decorated function.
    :param func :the function to decorate
    :return:  The wrapper function that adds the print() statements
    """
    def wrapper(n):
        print("Calculating the Fibonaci numbers..")
        result = func(n)
        print(f"fibonacci numbers are:\n{result}")
        return result
    return wrapper

#make use of the above decorator
@fibonacci_decorator
def generate_fibonacci_number(n):
    """
    Generate a list of fibonacci numbers up to n using the fibonacci() function.
    :param n: (int) The n-th Fibonacci number.
    :return: A List of fibonacci numbers
    """
    return [fibonacci(a) for a in range(n)]


#call invoke the generate fibonacci numbers
generate_fibonacci_number(7)

print("\n")

generate_fibonacci_number(18)
