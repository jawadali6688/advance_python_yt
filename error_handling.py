# value1 = 10

# value2 = 5

# try:
#     print(value1 / value2)

# except ZeroDivisionError:
#     print("You cannot divide a number by zero")

# try:
#     print(value1 / value2)

# except:
#     print("There is an error")
# # except ZeroDivisionError:
# #     print("There is zeror division")
# else:
#     print("Successfully programmed")

# finally:
#     print("final execution")

# print("Hello Jawad")



def calculate_age(user_age):

    try:
        if user_age == 0:

            raise Exception("Invalid user age.")
    
        else:
            print("Valid age")

    except Exception as e:
        print(e)

calculate_age(0)
