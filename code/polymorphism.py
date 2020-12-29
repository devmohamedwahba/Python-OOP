def multiply(first_num, second_num, multiplier=1):
    print(first_num * second_num * multiplier)


class Animal:
    def __init__(self):
        pass

    def fly(self):
        print('fly............')

    def eat(self):
        print('eat ..............')


class Duck(Animal):
    def fly(self):
        print('cant fly............')


if __name__ == "__main__":
    # multiply(1, 2, 3)
    duck = Duck()
    duck.fly()
