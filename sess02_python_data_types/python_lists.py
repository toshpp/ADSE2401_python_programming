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


#Display  the last 2 fruits in the list
print(f"the last 2 fruits list are : {fruits[-2:]}")

#Display every 2nd fruit starting from thr 2nd one in the fruit list
print(f" Starting from the second fruit and skipping one fruit we get: \n{fruits[1::2]}")

#Display the fruit list in reverse order without using thr reverse() function
print(f"The reversed list of fruits is: \n{fruits[::-1]}")

# TODO: display every 3rd fruit in the fruit list

#Display all the fruits from the first and last one
print(f"All the  fruits  in the list apart fron the first and last one are: \n{fruits[1:-1]}")

# Dispaly inreverse order starting from the 3rd last fuit
print(f"All the  fruits in reverse order stating from the 3rd last fruit are: \n{fruits[-3::-1]}")

#get and display an empty slice from the frruit list
print(f"The empty slice from list is : \n{fruits[len(fruits)-1:3]}")



