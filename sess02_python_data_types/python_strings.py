#python script to demonstrate string functions in python

#Declare a string variable

string_var = "hello Irungu from python programming"
# Display the string variable
print("'string_var' with the first letter capitalised is: %s" %string_var.capitalize())
print(f"'string_var' with the first letter capitalised is: %s:{string_var.capitalize()}")

#display the type of 'string_var'
print(f"the type of ;string_var' is: {type(string_var)}")

#display the contents of 'string_var' in uppercase
print(f"the contents of 'string_var' in uppercase is: {string_var.upper()}")

#display the contents of 'string_var' in lowercase
print(f"the contents of 'string_var' in lowercase is: {string_var.lower()}")

string_2_center ="programming"
#center the above  text with a specified width and given fill character
print(string_2_center.center(32))

#count  & display the number of times a character appears in  string ('o' in 'string_var')
print(f"The letter 'o' appears {string_2_center.count('o')} times in '{string_var}")

#Display the highest and lowest alphabetical characters (using ASCII codes
print(f"The highest and lowet alphabetical character in '{string_var}' are:"
      f"'{max(string_var)}' &' {min(string_var)}'respectively")

#Replace the 'he' with 'He' and 'python' with 'C#'
new_str =string_var.replace("He ","He")
new_str =new_str.replace("Python ","C#")

#Display the replaced/modified string
print(f"The modified contents of 'string_var' are: {new_str}")

#Declare another string variable for more string operations
my_string ="Hello, world 123"

#get and display the number of characters using len()
print(f"length of the string \'n'{my_string}' is {len(my_string)} characters")
#isalnum() -checks if all characters are alphanumeric(no spaces symbols)
print(f"is the string \n{my_string} alphanumeric? {my_string.isalnum()}")

#is lower() -checks if all alphabetic characters are lowercase
print(f" is the string \n{my_string} all lowercase?{my_string.islower()}")

#is Upper() -checks if all alphabetic characters are lowercase
print(f" is the string \n{my_string} all uppercase?{my_string.isupper()}")

#lstrip() - removes any leading whitespace (from thr left)
print(f" removes the leading spaces from '{my_string}' to get : \n{my_string.lstrip()}")

#lstrip() - removes any leading whitespace (from thr right)
print(f" removes the leading spaces from '{my_string}' to get : \n{my_string.rstrip()}")


#strip() - removes any leading whitespace (from left and right)
print(f" removes the leading and trailing spaces from '{my_string}' to get : \n{my_string.strip()}")

#endswith()- checks if the specified string ends with the specified substring
print(f"Does the string '{my_string}'end with '123'? {my_string.strip().endswith('123')}")

#find() -locates the first occurence of the specified substring
print(f"The first occurence of the string 'world' in {my_string} is at index:"
      f"{my_string.index('world')}")

#index() - finds the first occurence of the substring  raises errors when not found
print(f"Index of 'world'" ,my_string.index('world'))

#count() -counts the number of occurence of the substring or character
print(f"The number of occurrences of "or" in '{my_string}' is : {my_string.count('or')}")

#rfind() - finds the last occurence of the specified substring
print(f"the last occurence of 'l' in " ,my_string.index('world'))

#rfind thr last occurence of the specified substring, raises error when not found
print(F"the last index of'l' '{my_string}' is at index: {my_string.index('l')}")

#startswith()-check if the string stats with the given substring (prefix)
print(f'Does the string "{my_string}" starts with "  ' Hello'? "{my_string.startswith("..Hello")}')


