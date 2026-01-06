"""
python tuples
A tuple is a builtin data type that represents an ordered collection of elements of the same type
Tuples allow duplicates and are immutable (their elements cannot be modified)
tuples are created using () rounded brackets/parentheses or tuple() constructor


"""

#craeete a tuple of fruits
fruits = ("blueberry","orange","apple", "banana", "cherry","avocado","guava")

#diaplay the fruits in the tuple and their number
print(f"the fruits in the tuple are: {fruits}.\n"
      f"the number of fruits in the tuples is: {len(fruits)}")

# get and display the index of an ite/element in the tuple
print(f"The index of 'avocado' is {fruits.index('avocado')}")

#get and display the number of occurrences of blueberry in the tuple
print(f"'blueberry' appears {fruits.count('blueberry')} times in the fruit tuple.")

# combine two tuples to create a third one and display its contents
combined_fruits = fruits + ("kiwi", 'watermelon', "pineapple", 'dragon fruit')
print(f"The combined fruits tuple contain: \n{combined_fruits}")

#create a tuple that repeats the fruit tuple twice
fruits_repeated = fruits * 2
print(f"The 'fruits_repeated' tuple contain: \n{fruits_repeated}")

#craeete a sorted tuple of fruits
sorted_fruits =sorted(fruits)
print(F"The sorted fruits tuple contain: \n{sorted_fruits}")

#Display the minimum and the maximum tems (fruits) ina tuples (least and highes fruits letterwise)
print (f"the least fruits letterwise is {min(fruits)}"
       f"the highest fruits letterwise is {max(fruits)}")

#declare a tuple of numbers
numbers =(1,2,3,4,5)

#displaty the tuple numbers and its sum
print(f"The 'numbers' tuple contain: \n{numbers} and their sum is:{sum(numbers)}")

#display the first 3 numbers in the tuple
print(f'the first 3 numbers in the "numbers" tuple are: {numbers[:3]}')

#display only the odd numbers from the numbers tuple
print(f"The odd numbers in the 'numbers' tuple are:{numbers[::2]}") #same ad {numbers[0::2]}

#use the 'any()' function to check if any element in the 'numbers' tuple is true
#in python non-zero numbers are considered true.since all numbers in the tuple are non-zero
#'any(numbers)' will return True

any_true=any(numbers)
print(f"There only non-zero numbers in the 'numbers' tuple are: {any_true} using 'any()'")

#use the 'all()' functions to check if all elements in the numbers tuple are true
#Since all elements (1,2,3,4,5) are non-zero, they are all considered true
#so 'all(numbers) will also return true

print(f"there only non-zero in the numbers tuple are: {all(numbers)} using 'all()'
      