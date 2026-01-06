# python script to demonstrate how to create, write and read from a text

# import the os module
import os  # Module enables our script to work with the operating system (OS) and its file system

# create a function to create and write to a file
def create_file(path, content):
    """
    Create a file with the given path and write the specified content to it.

    param path (str): the path of the file to be created
    param content (str): the content to be written to the file
    """
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
        print("File created and content written successfully")


# get and display the current working directory
current_dir = os.getcwd()
print(f"Current working directory:\n{current_dir}")

# get and display the path to the files by going up one folder
file_directory = os.path.abspath(os.path.join(current_dir, '..', "files"))
print(f"The path to the File directory:\n{file_directory}")

# specify and display the full file path
file_path = os.path.join(file_directory, 'hello.txt')
print(f"The full path to the file created is:\n{file_path}")

# ensure the 'files' directory exists
os.makedirs(file_directory, exist_ok=True)

# specify the content
content = "hello from text files in python!!"

# call and invoke the create_file() function
create_file(file_path, content)

#write code to read the contents of the 'hello text' file and display them