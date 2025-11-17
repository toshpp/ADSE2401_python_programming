#python scripts to demonstrate the various arithmetic operations on numeric values

#Declare and get two values for the user

num1 = int(input("Enter first number to be used in the calculations: \n"))
num2 =int(input("Enter second number to be used in the calculations :\n"))

# Addition
sum = num1 + num2

#Subtration
difference = num1 - num2

#Product
product = num1 * num2

#Division
floating_division = num1 / num2
integer_division = num1 // num2

#modulus
modulus = num1 % num2

#Exponentiation
exponent = num1 ** num2

#Display the results
print(f"Addition; {num1} + {num2} = {sum}")
print(f"Subtraction; {num1} - {num2} = {difference}")
print(f"Multiplication; {num1} * {num2} = {product}")
print(f"Division; {num1} / {num2} = {floating_division}")
print(f"Integer Division; {num1} // {num2} = {integer_division}")
print(f"Modulus; {num1} % {num2} = {modulus}")
print(f"Exponent; {num1} ** {num2} = {exponent}")



