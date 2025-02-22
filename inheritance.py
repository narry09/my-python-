class Animal():
    def __init__(self):
        print("Animal created")
    def who_am_i(self):
        print("I am an animal")
    def eat(self):
        print("I am eating")


class Dog(Animal):
        def __init__(self):
            Animal.__init__(self)
            print("Dog Created")
        def who_am_i(self):
            print("I am a dog")
        def bark(slef):
            print("whoof")

my_dog=Dog()
my_dog.who_am_i()
my_dog.bark()
my_dog.eat()