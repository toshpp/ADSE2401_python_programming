"""
python dictionaries
This is built in data type that represents collection of key-value pairs, like dictionary
where each word has a corresponding definition
Dictionaries are unordered , mutable and can store elements of different types

"""

#Student dictionary declaration
student ={"name":'peter;',"age": 20, "major":'python'}

#display the length (number of key value pairs) of the student dictionary
print(f" the number of key-value pairs in the 'student' dictionary: is {len(student)}")

#fetch and display a view object (method to get the keys or value from a dictionary)
#of the keys in the 'student' dictionary
print(f'the keys from the "student" dictionary are : \n{student.keys()}')

#fetch and display a view object of the value in the 'student' dictionary
print(f'the value from the "student" dictionary are : \n{student.values()}')

#fetch and display a view object of the contents in the 'student' dictionary
print(f'the contents from the "student" dictionary are : \n{student.items()}')

#Get and display a value using its key from thr 'student' dictionary
print(f'The key "name" in the "student" dictionary points to: {student["name"]}') #student.get("name)

#Remove and display the contents  of a given key when it exists dina dictionary
#else return/give back an optional default value
phone_no = student.pop("phone_no", "Not specified")
print(f"the value of 'phone_no' in the  'student' dictionary is : {phone_no}")

#Remove and display the contents  of the last key-value pair in the 'student' dictionary
print(f"The last key-value pair in the 'student' dictionary is : {student.popitem()}")

#Update/modify and display the contents of the 'student' dictionary
student.update({"aeg":21,  "grade":'A', "phone":"o7123455677"})
print(f"The updated contents for the 'student' dictionary are :\n{student.items()}") #0r {student}

#create and copy of the "students" dictionary
copy_of_student=student.copy()
print(f"The contents of 'copy_of_student' are :\n{copy_of_student.items()}")

#fetch and return the value associated with a given key when not found assign with a defaul value
major =student.setdefault("major","not defined")
print(f"The value of the key 'major' in the 'student' dictionary is : {major}")

#create and display a new dictionary for the keys of an existing dictionary
new_student =dict.fromkeys(student.keys()) #new_student =dict.fromkeys(["name","age","grade","phone"]

#Delete a specific key-value from the 'student' dictionary
#and display the remaining key-value pairs
del student['grade']
print(f"After removing/deleting the 'grade' key from the 'student' dictionary,the remaining key-value"
      f"pairs are:\n{student}")

#find out and display whether a given key exists/is present in dictionary
print(f'the key "age" is present  in teh "student" dictionary: {"age" in student}')
print(f'the key "grade" is present  in teh "student" dictionary: {"grade" in student}')


#remove all the content from the student dictionary and display
student.clear()
print(f"After clearing the 'student' dictionary we get :\n{student}")

