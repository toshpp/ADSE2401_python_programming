# python script to create a simple tkinter GUI calculator for addition, multiplication, subtraction and division

# import the required modules
import tkinter as tk
from tkinter import messagebox, ttk  # ttk is for the combobox


# Define a function to read in the values from the user
def calc():
    # Get the numbers and operation from the entry fields and combobox respectively
    first_number = entry_first.get()
    second_number = entry_second.get()
    operation = entry_operation.get()

    # Check if any of the above fields are empty
    if not first_number.strip() or not second_number.strip() or not operation.strip():
        messagebox.showerror("Missing Values or Operation",
                             "Please enter all values and the arithmetic operation")
        return

    try:
        # Convert the values from input fields to numbers
        first_number = int(first_number)
        second_number = int(second_number)
    except ValueError:
        messagebox.showerror("Invalid Values",
                             "Please enter valid numeric values for first & second number.")
        return

    # Check for division by zero
    if operation == "/" and second_number == 0:
        messagebox.showerror("Divide by Zero Error",
                             "Cannot divide by zero '0'. Please enter a non-zero denominator.")
        return

    # Define the arithmetic operator mappings
    operations = {
        '+': first_number + second_number,
        '-': first_number - second_number,
        'x': first_number * second_number,
        '/': first_number / second_number,
    }

    # Check whether the operation is valid and show the result
    if operation in operations:
        result = operations[operation]
        label_answer.config(text=f"Result:  {result}")
    else:
        messagebox.showerror("Invalid Operation",
                             "Please choose a valid operation (+, -, x, or /).")


# create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("640x480")
root.resizable(False, False)

# created a centered frame
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor='center')

# Labels
label_first = tk.Label(frame, text="First Number:")
label_first.grid(row=0, column=0, padx=10, pady=10, sticky='e')

label_operation = tk.Label(frame, text="Operation (+, -, x, /):")
label_operation.grid(row=1, column=0, padx=10, pady=10, sticky='e')

label_second = tk.Label(frame, text="Second Number:")
label_second.grid(row=2, column=0, padx=10, pady=10, sticky='e')

label_answer = tk.Label(frame, text="Result:")
label_answer.grid(row=3, column=0, padx=10, pady=10, sticky='e')

# specify the width for the input widgets
input_width = 25

# Entry for first number
entry_first = tk.Entry(frame, width=input_width)
entry_first.grid(row=0, column=1, padx=10, pady=10)
entry_first.insert(0, "Enter first number")
entry_first.focus()

# Dropdown combobox for the desired arithmetic operation
operation_choices = ['+', '-', 'x', '/']
entry_operation = ttk.Combobox(frame, values=operation_choices,
                               state='readonly', width=input_width - 3)
entry_operation.grid(row=1, column=1, padx=10, pady=10)
entry_operation.set("Select Operation")

# Entry for second number
entry_second = tk.Entry(frame, width=input_width)
entry_second.grid(row=2, column=1, padx=10, pady=10)
entry_second.insert(0, "Enter second number")

# Calculate button
btn_calc = tk.Button(frame, text="Calculate", width=20, command=calc)
btn_calc.grid(row=3, column=1, padx=10, pady=20)

# Run the GUI main loop
root.mainloop()





