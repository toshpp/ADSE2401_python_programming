# python script to demonstrate the scope of global and local variables

#DEclare a global variable
global_var =5

#define a function to display the value passed to it
def  display_value(value):
    print(f"The value passes in is: {value}")
    #call the display_value function and pass in the global variables(global_var)
display_value(global_var)

def random_function():
    random_variable ="Hello" #random_variable is only accessible within random_function
    return random_variable

#call random_function() to get the local variable
random_variable = random_function()

#call the display_value function and pass in the random variable
display_value(random_variable)
