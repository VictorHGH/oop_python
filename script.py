class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof woof!")


dog1 = Dog("fido", "labrador")
dog1.bark()

dog2 = Dog("spot", "labrador")
dog2.bark()
