# The script demonstrates pythons iteration/repetition /looping constructs
from sess02_python_data_types.python_numeric_types import false_value

# --------------------------------------
# 1. for loop
#

#create a list of fruits
fruits =["kiwi", 'watermelon','pineapple',"strawberry", 'banana',
         "mango","blackberry","blueberry","grapes",'guava', 'Orange','passion'
         'date,', 'tomato','apple']

#diplay each of the above fruits using a 'for' loop
for fruits in fruits:
    print(F"The current fruit is {fruits}")

#create a list of numbers and display them using a for loop
numbers =[8,2,5,7,12,40,39,17,1,100,22]
for num in numbers:
    print(f"The current number is {num}")

# --------------------------------------
# 2. range
#
print(f"range".center( 42,"-"))

#basic range: generate the first 5 numbers
for n in range (5) :#basic range starts from 0 to a specified number minus 1
    print(f"the current number is {n}")

print(f"range with parameters".center( 42,"-"))

#generate even numbers stating from 2-10(exclusive) using range with start stop amd
for n in range(2,10,2):
    print(f"the current number is {n}")

cubes =[n **3 for n in range(1,6)]
print(f"the cubes of the first 5 integers are \n{cubes}")


# --------------------------------------
# 3. while loop
#

print(f"while loop".center( 42,"-"))
#Display the first 5 multiples of 8
n =1
print("the first multiples of 8 are:")
while n <=5:
    print(f"{n} * 8= {n*8}") #%d is a format specifier for integers
    n +=1

#create a list of even  numbers
n, even_nums= 1, []
print("The even numbers between 1-20 are:")
while n <=20:
    if n % 2 == 1: #when the number is odd (same as if in n % 2 !=0)
        n+=1
        continue #skip the current iteration when the number is odd
    even_nums.append(n)
    n+=1
#display the list of even numbers
print(even_nums)


#practical use of a while loop to search for some text
paragragh = """
Video provides a powerful way to help you prove your point. When you click Online Video, 
you can paste in the embed code for the video you want to add. You can also type a keyword 
to search online for the video that best fits your document. To make your document look professionally
 produced, Word provides header, footer, cover page, and text box designs that complement each other. 
 For example, you can add a matching cover page, header, and sidebar. Click Insert and then choose the elements you want 
 from the different galleries. Themes and styles also help keep your document coordinated. When you click Design and choose
  a new Theme, the pictures, charts, and SmartArt graphics change to match your new theme. When you apply styles, your headings c
  change to match the new theme. Save time in Word with new buttons that show up where you need them.


""".lower()#converts to lower/upper for case insensitive search
#variable to hold the word
text_to_ssearch ="theme"
found =False
index=0

while index < len(paragragh):
# find the index of the word/search text
if paragragh[index: index + len(text_to_ssearch)] == text_to_ssearch:
    found=True
    break # exit the while loop
    inde +=1
if found:
    print(f")


