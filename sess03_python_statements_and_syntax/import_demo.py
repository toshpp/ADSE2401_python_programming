#python script demonstrating how to import a module and use its code in the current script

#import (bring_in) the code from the greetings module
from greetings import greet

#prompt the user for their name
username= input("Please enter your name: ")

#use the function from the greeting module to greet the user
print(greet(username))
