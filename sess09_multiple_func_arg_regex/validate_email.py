# import the required modules
import re
import tkinter as tk
from tkinter import messagebox, END

# function to validate email address
def validate_email():
    email = entry_email.get().strip()

    if email == "":
        messagebox.showerror("Missing Email Address",
                             "Please enter your email address to be validated")
        return

    pattern = r"^[a-zA-Z\d.+-]+@[a-zA-Z\d.]+\.[a-zA-Z]+$"

    if re.match(pattern, email):
        messagebox.showinfo("Valid Email Address",
                            "The email address is valid!")
    else:
        messagebox.showerror("Invalid Email Address",
                             "The email address entered is not valid!")

# function to clear the email address entry widget
def clear_text():
    entry_email.delete(0, END)

# set up the GUI
root = tk.Tk()
root.title("Validate Email Address")

# label
label_email = tk.Label(root, text="Email Address")
label_email.grid(row=0, column=0, padx=10, pady=5)

# entry field
entry_email = tk.Entry(root)
entry_email.grid(row=0, column=1, padx=10, pady=5)

# buttons
button_validate = tk.Button(root, text="Validate Email", command=validate_email)
button_validate.grid(row=1, column=0, padx=10, pady=5)

button_clear = tk.Button(root, text="Clear Email", command=clear_text)
button_clear.grid(row=1, column=1, padx=10, pady=5)

# run the application
root.mainloop()
