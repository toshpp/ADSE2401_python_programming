# This script demonstrates python's selection/decision/conditional constructs

# import the sys (system) module
import sys

# --------------------------------------
# 1. if
#

temperature = float(input("please enter today's temperature in Celsius: "))
if temperature > 25:
    print("Hooray its sunnyday")

password = "xeefe"
if password == "":
    print("please enter your password")
5
# --------------------------------------
# 2. if ...else
#

user_num = int(input("please enter a number and I'll tell you if it's odd or even: \n"))
if user_num % 2 == 0:
    print(f"{user_num} is an even number")
else:
    print(f"{user_num} is an odd number")

score = int(input("please enter your score: \n"))
if score >= 40:
    print(f"Congratulations! With a score of {score} you've passed.")
else:
    print(f"Unfortunately, with a score of {score} you've failed the exam.")

# --------------------------------------
# 3. if ...elif(else if)..else

# Grade the student based on the score entered above
if score >= 70 and score <= 100:
    print(f"With a score of {score} you got grade 'A'")
elif score >= 60:
    print(f"With a score of {score} you got grade 'B'")
elif score >= 50:
    print(f"With a score of {score} you got grade 'C'")
elif score >= 40:
    print(f"With a score of {score} you got grade 'D'")
elif score >= 0:
    print(f"With a score of {score} you got grade 'E'")
else:
    print(f"Sorry, {score} is not a valid score. "
          f"Please enter a score between 0 and 100.")
    sys.exit()  # terminate the script

# --------------------------------------
# 4. match
# Nb: match works in python version >= 3.10 only

# prompt the user for a day of the week
day = input("please enter a day of the week: ")

match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print(f"{day} is weekday")
    case "Saturday" | "Sunday":
        print(f"{day} is weekend")
    case _:
        print(f"sorry, {day} is not a valid day of the week")
        sys.exit()  # terminate script

# Give the student a comment based on their score using match
match score:
    case _ if score >= 70:
        print("Excellent job!")
    case _ if score >= 60:
        print("Very good!")
    case _ if score >= 50:
        print("Good effort!")
    case _ if score >= 40:
        print("You passed!")
    case _:
        print("You need to work harder.")
