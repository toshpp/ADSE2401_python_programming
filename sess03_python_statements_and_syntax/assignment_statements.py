# python scripts to demonstrate assignment statement

# basic assignments
num1 = 5
spam = 'Yim'
print(f"the contents of 'num1' and 'spam' are {num1} and {spam}")

# tuple assignments
spam, ham = 'Spam', 'YUM'
print(f"The contents of 'spam' and 'ham' variables after tuple assignments are {spam} and {ham}")

# list assignment (positional)
car, drink = ["cx5", "juice"]
print(f"The contents of 'car' and 'drink' variables after list assignment are {car} and {drink}")

# sequence assignment for numeric values
first_num, second_num, third_num, fourth_num = [5, 8, 4, 7]
print(f"the contents of 'first_num', 'second_num', 'third_num' and 'fourth_num' are "
      f"{first_num}, {second_num}, {third_num}, {fourth_num}")

# sequence assignment for alphanumeric values
# string "CX-5" contains 4 characters: 'C','X','-','5'
first_car, second_car, third_car, fourth_car = "CX-5"
print(f"the contents of 'first_car', 'second_car', 'third_car' and 'fourth_car' are "
      f"{first_car}, {second_car}, {third_car}, {fourth_car}")

# Extended sequence assignment for numeric values
first_num, second_num, *other_nums, eighth_num = [5, 8, 4, 7, 12, 3, 1, 12]
print(f"the contents of 'first_num', 'second_num', 'other_nums' and 'eighth_num' variables are "
      f"{first_num}, {second_num}, {other_nums}, {eighth_num}")

# Extended sequence assignment for alphanumeric values (string unpacking)
first_num, second_num, *other_nums, eighth_num = "meatball"
print(f"the contents of 'first_num', 'second_num', 'other_nums' and 'eighth_num' variables are "
      f"{first_num}, {second_num}, {other_nums}, {eighth_num}")


#multiple target assignment
print(f"the contents of 'first_num', 'second_num', 'third_num' variables before multiple target assignments are {first_num}, {second_num}, {third_num}")
first_num = second_num=third_num = 8
print(f"the contents of 'first_num', 'second_num', 'third_num' variables after multiple target assignments are {first_num}, {second_num}, {third_num}")

#argument assignment(
second_num +=


