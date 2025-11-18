"""
python sets
A set in python is a builtin type that represents an unordered collection of elements of the same  or different types
sets don't allow duplicates and are mutable. They are suitable for tasks that involve checking membership,
removing duplicates and performing operations like
intersection, union,differences, and systematic_difference
Sets are created using the curly braces{} or set () constructor """

#Crweate a set of fruits
fruits = {"apple", "banana", "cherry",'durian','elephant apple'}

#display the contents of the fruits set
print(f"the fruits in the fruits set are :\n{fruits}")

#display the number of fruits in the fruits set
print(f"the fruits set contains : {len(fruits)} fruits")

#add 'orange' to the fruits set
fruits.add('orange')
print(f"After adding 'orange' to fruits set  we get: \n{fruits}")

#remove 'banan' from the fruitset
fruits.remove('banana')
print(f"After removing 'banana' to fruits set  we get: \n{fruits}")

#discard "cherry" from the fruit set
fruits.discard('cherry')
print(f"After removing 'cherry' to fruits set  we get: \n{fruits}")

#remove the last item (fruits) from a set
popped_fruit=fruits.pop()
print(f"After popping  {popped_fruit} from the fruit set we get: \n{fruits}")

#copy the set of remaining fruits to a new set and display them
copy_of_fruits =fruits.copy()
print(f"After copying the remaining fruits to  a  new set we get : {copy_of_fruits}")

#declare another set of fruits
more_fruits = {'pearl', 'avocado', "mango", "pineapple"}

#create a new combined set of fruits and display it
combined_fruits = fruits.union(more_fruits)
print(f"the combined set of fruits is :\n{combined_fruits} ")

#get and display the common fruits in the 'combined_fruits' and 'more_fruits' sets & display theme
common_fruits = combined_fruits.intersection(more_fruits)
print(f"the common set of fruits in 'combined_fruits' and 'more_fruits' are :\n{common_fruits}")

#get and display the fruits that are in 'fruits' set but not in 'more_fruit' set
different_fruits =fruits.difference(more_fruits)
print(f'The fruits in the "fruit" set but not in the "more_fruits" set are :\n{different_fruits}')


#get and display the fruits that are either in 'fruits' or 'more_fruits' set but not in both
symmetric_diff_fruits = fruits.symmetric_difference(more_fruits)
print(f'The fruits are either in "fruits" dset or"more_fruits" set but not both are :\n{symmetric_diff_fruits}')

#checked and display whether  fruit set is a subset of "more_fruits"
print(f"'fruit' set is a subset of 'more_fruits': {fruits.issubset(more_fruits)}') '")

#checked and display whether  fruit set is a superset of "more_fruits"
print(f"'fruit' set is a superset of 'more_fruits': {fruits.issuperset(more_fruits)}') '")

#check and display whether 'fruit' set and 'more_fruit' set have no common fruits/element
is_disjoint_fruits = fruits.isdisjoint(more_fruits)
print(f"'fruit' set and 'more_fruits' set have no common fruits/elements: {is_disjoint_fruits}")

# Create another fruit set and use it to update the set of fruits: CAUTION...overwrites set elements
other_fruits ={'watermelon','strawberry', 'blueberry'}
fruits.update(other_fruits)
print(f'after updating the "fruits" set we get: \n{fruits}')

# clear and display the 'fruits' set
fruits.clear()
print(f"After clearing the 'fruits' set we get: \n{fruits}")



