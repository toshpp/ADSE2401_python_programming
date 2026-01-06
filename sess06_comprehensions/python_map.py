# python script/file to demonstrate the map() function

# set of Fibonacci numbers
numbers = sorted(set([1,1,2,3,5,8,13,21,34,55,89,144]))

#Get and display the triple of each of the fibonacci
tripled_num = sorted(set(map(lambda x: x * 3, numbers)))

print(f"Set of fibonacci numbers :\n{numbers}"
      f"\nTriples of fibonacci numbers :\n{tripled_num}")

#List of names and ages
names =['Abigail','bernci','charlene','Denise']
ages =[21,24,22,19]


#use the map function to combine the above names and ages for each person
combined_data = map(lambda name,age: name + age, names, ages)

#Convert the combined map 
