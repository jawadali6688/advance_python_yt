
# def login_checking(func):

#     def wrapper(username):
#         if username != "Jawad12":
#             return print("Invalid Username")

#         func(username)

#     return wrapper


# @login_checking
# def login(username):
#     print(f"Hey {username}, Welcome to Dashboard")

# login("Jawad12")

# import time

# def function_checking(func):

#     def wrapper():
#         start_time = time.time()
#         print("Executing the function")
#         func()
#         print("Execution of function ended")
#         end_time = time.time()
#         print(f"Execution start time is: {start_time}")
#         print(f"Execution end time is: {end_time}")

#     return wrapper

# @function_checking
# def greet():
#     print("Hello Jawad")

# greet()


# def login_checking(func):

#     def wrapper(*args, **kwargs):

#         print(args)
#         print(kwargs)

#         func(*args, kwargs)

#     return wrapper

# @login_checking
# def login(*args, **kwargs):
#     pass

# login("jawad", "khan", roll="01003", depart="ai")