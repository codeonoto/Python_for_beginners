class Parent:
    def __init__(self):
        print("This is the parent class")


class Child(Parent):
    def __init__(self):
        super().__init__()
        print("This is a child class")


class ChildChild(Child):
    def __init__(self):
        super().__init__()
        print("This is a ChildChild Class")


child1 = ChildChild()
