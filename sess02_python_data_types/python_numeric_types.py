# python script to demonstrate Pythons number/numeric types

#Get the code to make eDecimal numbers work

from decimal import Decimal ,getcontext, ROUND_DOWN

#Get the code to make Fractions numbers work
from fractions import Fraction

#Demonstrate integers (whole numbers, both+ve and -ve

int_value =8
print("integer demonstration")
print (f"-"*22)
print (f"The value in the variable  int_value is{int_value}")
print (f"(The value of int_value is {type(int_value)}\n")

#Demonstrate floats/floating point numbers (numbers with a fractional component, both +ve and -ve)

float_value = 3.1415927
print("Floating-point Number Demonstration")
print (f"-"*22)
print (f"The value in the variable  float_value is {float_value}")
print (f"The value in the variable  float_value correct to 4 d.p is {float_value:.4f}")
print ("The value in the variable  float_value correct to 4 d.p is %.4f" %float_value)
print (f"(The value of float_value is {type(float_value)}\n")

#Demonstrate Decimal(with decimal places and a fixed precision , both -ve and positive)
# Ser the precision for decimal operations

getcontext().prec=7 #set a higher precision when u need to maintain accuracy
# for rounding numbers with lots of decimal places e.g Decimal ('345.234567890123456789')
decimal_value =Decimal(8.1415933892)
print ('Decimal Number Demonstration')
print ("-"*32)
print (f"The original value of  'decimal_value' is {decimal_value}")
#Using ROUND_DOWN to ensure no rounding up takes placce
decimal_value =Decimal('1.234567890122345678').quantize(Decimal('0.0001'),rounding=ROUND_DOWN)
print (f"the modified value of 'decimal _value' correct to four d.p is :{decimal_value}")
print(f"The type of 'decimal_value' is {type(decimal_value)}\n")

#demonstrate Complex Numbers
complex_value =3 +4j
print(f"Complex Number Demonstration")
print ("-"*32)
print(f"the value of 'complex_value' is {complex_value}")
print(f"The type of 'complex_value' is {type(complex_value)}\n")
print(f"the real part of the value of 'complex_value' is {complex_value.real}")
print(f"The imaginary part of the value of 'complex_value' is {complex_value.imag}")

#Demonstrate Fraction (rational numbers)
fraction_value = Fraction(7, 3)
print("Fractional Number Demonstration")
print (f"-"*32)
print(F"The value of 'fraction_value' is {fraction_value}")
print(f"The type of 'fraction_value' is {type(fraction_value)}")

#Demonstration Boolean (True or False)
true_value = True
false_value = False; n =5; a = 8 #How to declare multiple variable on a single line python
print(f"Boolean Value Demonstration")
print (f"-"*32)
print(f"Boolean value in 'true_value' is {true_value}")
print(f"Boolean value in 'false_value' is {false_value}")
print(f"The type of 'true_value' is {type(true_value)}, and 'false' is {type(false_value)}")
print(f"Using Boolean in arithmetic operations")
print(f"-"*32)
print(f"True + True ={true_value + true_value}")
print(f"True + False ={true_value + false_value}")
print(f"False + False= {false_value + false_value}")
print(F"False + n(5) is {false_value + n}")
print(f"True  +a(8) is :{true_value + a}")
print(f"True *n(5) is {true_value * n})")
print(f"(n < a) * 10 + (n== a) * 20 is :{(n < a) * 10 + (n== a) * 20}")