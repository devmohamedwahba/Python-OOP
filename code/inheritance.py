class Animal:
    def __init__(self, name):
        self.name = name
        self.no_of_legs = 4

    def __str__(self):
        return self.name


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name=name)


if __name__ == '__main__':
    dog = Dog('kiki')
    print(dog)
