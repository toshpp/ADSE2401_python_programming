#python script to validate a kenyan phone number using a regular expression(s) : regex

#import the regex (regular expression) module
import re

#function to validate the phone number
def validate_phone_number(phone_number):

    #Python raw string with a regex to match the kenyan number
    pattern =r"\+254\s?([1-7\d\d)\s?(\d){6,7}"

    if not phone_number:
        print("Please enter YOR phone number")
        return

    #compare the input phone number and the pattern and display an apt message
    if re.match(pattern, phone_number):
        print(f"The number {phone_number} is a valid kenyan phone number")

    else:
        print(f"The number {phone_number} is not kenyan phone number")


#prompt the user for their number
phone_num =input(" please enter your phone number, and ill tell you if its valid"
                 "Kenyan phone number::/n")

# Validate the users phone numer
validate_phone_number(phone_num)


