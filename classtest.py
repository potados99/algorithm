class Person:
    age = 0
    name = "NONAME"

    def __init__(self):
        print("I AM BORN")

    def show_your_self(self):
        print("age: " + str(self.age))


    def __str__(self):
        self.age += 1
        return "I am " + self.name + ", I am " + str(self.age) + " year(s) old."


if __name__ == "__main__":
    pass
