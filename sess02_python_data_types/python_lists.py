"""
Python lists
A python list is a built data type that represents an ordered collection of items/element, that are homogenous in nature
Lists allow duplicates and are mutable (ie .their elements can be modified added or removed
Lists are created using [] or the list() constructor
a sample list of its operations are given below
"""
from operator import index
from os import remove

#create a list of fruits
fruits =["apple","banana","cherry"]

#Display the fruits in the fruit list
print(f" the fruits are: {fruits }")


#Display the number of items/elements in the fruit list
print(f"the number of fruits in the fruits list is:{len(fruits)}")

#Add a fruit to the end of the fruit list
fruits.append("orange")
print(f"After adding orange to the fruits list we get : \n{fruits}")

#Add the contents of another list of fruits to our fruit list
fruits.extend(["mango",'grapes','kiwi','pineapple','strawberry','guava','avocado','apple'])

#display the combined list of fruits
print(f"the combined list of fruits is \n{fruits}")

#insert a fruit (item/element )at a given /specified index
fruits.insert(1,'pearl')
print(f"After inserting pearl to the fruits list we get : \n{fruits}")

#Remove a fruit (item/element) ata given/specified index
removed_fruit = fruits.pop(3)
print(f"The removed fruit is:{removed_fruit}")
print(f"After removing {removed_fruit} from the fruit list we get : \n{fruits}")

#Remove a specific fruit(item/element) from the List
fruits.remove("banana")
print(f"After removing 'banana' from the fruits list we get : \n{fruits}")

#Get and display the occurence(s) of a given item/element in the list
print(f"'apple' occurs {fruits.index('apple')} time(s) in the fruits list")

#sort and display the fruits lexicographipcal/alphabetical/ascending order
fruits.sort()
print(f"The list of fruits in ascending order : \n{fruits}")

#sort and display the fruits lexicographipcal/alphabetical/descending order
fruits.reverse()
print(f"The list of fruits in descending order : \n{fruits}")

#get and display the minimum and maximum items/element in the list
#(least and highest fruits letterwise)
print(f"The least fruits letterwise is :{min(fruits)}"
      f"\nThe highest fruits letterwise is :{max(fruits)}")
