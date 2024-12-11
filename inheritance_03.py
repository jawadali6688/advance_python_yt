class GrandFather:

    def __init__(self, name):

        self.name = name


    def show_name(self):

        print(f"Your Name is {self.name}")



class Father(GrandFather):  # class Father extends GrandFather
    pass


class Child(Father):
    pass

grand_obj = GrandFather("Grand")

father_obj = Father("Father")

child_obj = Child("Child")

child_obj.show_name()

father_obj.show_name()


grand_obj.show_name()
