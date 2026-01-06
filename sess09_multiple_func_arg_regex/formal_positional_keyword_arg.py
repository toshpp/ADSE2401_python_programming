# Python script to demonstrate the use of formal ,positional and keyword arguments in a function


# function definition
def profile (name, *args, **kwargs):
    print(f"Name: {name}")# formal argument
    if args:
        print(f"Hobbies:") #positional variable argument(s)
        for hobby in args:
            print(f"Hobby: {hobby}")
        if kwargs:
            print(f"Other info:")
            for key, value in kwargs.items():
                print(f"Key: {key},{value}")
#function call/invocation
profile("Irungu", "cooking","Eating","traveling", gender="male", age="20",
        password="30303@#1", job="Engineering",city="mombasa",country="USA")

#Formal arguments are defined in the function signature(name)
#*args: collects positional arguments as a tuple
#**kwargs :collects extra keyword arguments as a dictionary