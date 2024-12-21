# class Student:

#     def __init__(self, name, roll):
#         # self.name = name
#         # self.roll = roll   #public attributes

#         # self._name = name
#         # self._roll = roll   #private attributes

#         self.__name = name
#         self.__roll = roll   #protected attributes

#     def show_display(self):

#         print(self.__name)

# class Teacher(Student):

#     def __init__(self, name, roll):
#         super().__init__(name, roll)

#     def show_name(self, student):
#         print(f"Student name is {student.__name}")


# std1 = Student("Jawad", "01003")


# teacher1 = Teacher("Teacher", "01003")

# teacher1.show_name(std1)

# # print(std1.name)
# # print(std1.roll)



class Student:

    def __init__(self, name, roll):
        # self.name = name
        # self.roll = roll   #public attributes

        # self._name = name
        # self._roll = roll   #private attributes

        self.__name = name
        self.__roll = roll   #protected attributes

    # Getter method
    def show_display(self):

        print(self.__name)
        print(self.__roll)

    # setter method

    def change_roll(self, new_roll):
        self.__roll = new_roll
        print(self.__roll)

std1 = Student("Jawad", "01003")

std1.show_display()

std1.change_roll("01004")