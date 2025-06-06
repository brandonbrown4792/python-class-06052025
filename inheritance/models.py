class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("I'm eating")


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def speak(self):
        print(f"Woof, my name is {self.name} and I'm {self.age} years old")

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


    def speak(self):
        print(f"Meow, my name is {self.name} and I'm {self.age} years old")


animal = Animal('Barry')
dog = Dog('Spot', 1)
cat = Cat('Snickers', 2)

animal.eat()
dog.eat()
cat.eat()
dog.speak()
cat.speak()