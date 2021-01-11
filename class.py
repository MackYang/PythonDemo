class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

x=Dog("hhh")
print(Dog.kind)
print(Dog.__name__)
print(x.kind)
print(x.name)