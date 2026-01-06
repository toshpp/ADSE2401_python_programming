#python script to demonstrate simple comprehension operation on a set and dictionary

#A list of names and initials
names =['sam',"paul",'Nemo',"PAUL",'j','Nemo']
print(f"List of names and initials: {names}\n")

#obtain a set of unique names that have more than one character using a set comprehension
name_set = {name[0].upper() + name[1:] .lower()for name in names if len(name) > 1}

#Display the unique set of names
print(f"The unique names with more than one letter are {name_set}\n")

#Dictionary of the occurrences of different letters in the lower & uppercase form
test_dic = {'l' : 10,'b':34,'z':2,'N':4,'L':4,'Z':5}

#Display the Dictionary inits original form
print(f"Original letter count in the dictionary is {test_dic['l']}")

#Get and display the total occurrence of each letter regardless of the case using a dictionary comprehension
letter_count = {
    k.lower(): test_dic.get(k.lower(),0) + test_dic.get(k.upper(),0)
    for k in test_dic.keys()
        

}
print(f"The total count for each letter irregardless of case is:\n {letter_count}")