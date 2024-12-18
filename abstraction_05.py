from abc import ABC, abstractmethod


# Abstract class
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def show_name(self):
        pass


# Child class
class Dog(Animal):

    def work(self):
        print('Dog work')

    def sound(self):
        print("Dog sound method is abstract method")

    def show_name(self):
        print("My name is .....")


# animal_obj = Animal()

dog_obj = Dog()

dog_obj.work()

dog_obj.sound()

dog_obj.show_name()

