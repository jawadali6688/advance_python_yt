class Student:
    university = "IUB"

    def __init__(self, name):
        self.name = name

    def show_uni(self):
        return print(f"Uni: {self.university}")
    
    @classmethod
    def change_uni(cls, uni):
        cls.university = uni

    @staticmethod
    def mulitply(value1, value2):
        print(value1 * value2)

std1 = Student("Jawad")

std1.change_uni("KFUEIT")
std1.show_uni()
std1.mulitply(5, 2)