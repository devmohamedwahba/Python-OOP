class Foo:
    def __init__(self):
        self.public_name = "public"
        self._protected_name = "protected"
        self.__private_name = "Private"

    @property
    def private_name(self):
        return f'from function {self.__private_name}'

    @private_name.setter
    def private_name(self, name):
        self.__private_name = name


if __name__ == "__main__":
    fo = Foo()
    # can see from outside because it is public
    print(fo.public_name)
    # can see from outside but it tell developer that it cant be used from outside it only can be used from subclass
    print(fo._protected_name)
    # although it private but it can access from outside
    # it create new variable in class with same name
    print(fo._Foo__private_name)

    print(fo.private_name)

    fo.private_name = "test from outside"
    print(fo.private_name)
