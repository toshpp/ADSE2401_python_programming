## python script to demonstrate the filter() function

#List of Fibonacci numbers
numbers =[1,1,2,3,5,8,13,21,34,55,89,144]

#Get and display the list of odd fibonacci numbers using the filter() function
odd_fibonacci = list(filter(lambda x: x % 2 != 0, numbers))
print(f"Fibonacci numbers :\n {numbers}\n odd_fibonacci numbers:\n {odd_fibonacci}")

#set of student names
student_names = {
    "Abigail", "Bernci","Charlene","Denise","Sue","ji","mark","micha",
    "Alvin","Ann","Alice"


}
#use the filter() function to get snd display the names starting with 'A'
filtered_names = list(filter(lambda name:name.startswith('A'), student_names))
print(f"All student names:\n {student_names} \n student names starting with 'A'\n {filtered_names}")

#function to determine whether a number is prime or not
def is_prime(n):

    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):#same as for i in range(wint(math.sqrt(n)) +1
        if n % i == 0:
            return False
    return True

#set the range of numbers that we'd like to get prime numbers
num_range = range(1,70)

prime_numbers=list(filter(is_prime, num_range))
print(f"The prime numbers between 1 and 70 are:\n{prime_numbers}")
