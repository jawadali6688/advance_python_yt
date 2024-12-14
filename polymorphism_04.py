# class Person:

#     def __init__(self, name):

#         self.name = name

#     def show_name(self):

#         print(f"Your name is {self.name}")
    
#     def show_work(self):

#         print(f"Your work is empty")


# class Student(Person):

#     def show_name(self):

#         print(f"Your name is {self.name}")
    
#     def show_work(self):

#         print(f"Your work is Study")


# class Teacher(Person):

#     def show_name(self):

#         print(f"Your name is {self.name}")
    
#     def show_work(self):

#         print(f"Your work is Teaching")


# person_obj = Person("Person")

# std_obj = Student("Student")

# teacher_obj = Teacher("Teacher")


# person_obj.show_name()

# std_obj.show_name()

# teacher_obj.show_name()


# person_obj.show_work()

# std_obj.show_work()

# teacher_obj.show_work()



class Calculator:

    def add(self, num1=None, num2=None, num3=None):

        if num1 and num2 and num3:
            print(num1 + num2 + num3, "Sum")

        elif num1 and num2 and not num3:
            print(num1 * num2, "Mul")

        else:
            print(num1, num2, num3, "Nothing")


my_obj = Calculator()

my_obj.add(5, 10)