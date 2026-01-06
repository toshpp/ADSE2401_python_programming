# python script to demonstrate working with comprehensions

# List of Fibonacci numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

# Get and display the squares of the Fibonacci numbers
squares = [n ** 2 for n in numbers]
print(f"First 12 Fibonacci numbers:\n{numbers}\nFibonacci squares:\n{squares}")

# Get and display the cubes of the even Fibonacci numbers
cubes = [n ** 3 for n in numbers if n % 2 == 0]
print(f"Even Fibonacci numbers:\n{[n for n in numbers if n % 2 == 0]}\nEven Fibonacci cubes:\n{cubes}")

# Dictionary of students and their mean scores in an exam
student_scores = {
    'sue': 56,
    'jim': 61,
    'mark': 61,
    'micha': 55,
    'wiliam': 78,
    'jane': 51,
    'Zi': 56,
    'Abigail': 92
}

# Display the students and their scores
print(f"Students and their exam scores:\n{student_scores}")

# Get and display the dictionary of the students that passed (passmark: 55)
passed_students = {name: score for name, score in student_scores.items() if score > 55}
print(f"Students that passed and their exam scores:\n{passed_students}")

# TODO: Get and display the dictionary of students that failed
failed_students = {name: score for name, score in student_scores.items() if score <= 55}
print(f"Students that failed and their exam scores:\n{failed_students}")

# Extract and display the set of student names
student_names = set(student_scores.keys())
print(f"Set of student names:\n{student_names}")
