class Rectange:

    def __init__(self, height, width):
        self.height = height
        self.width = width
        print(f"A reactange is created with heigth: {height} and width: {width}")

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)


# h = int(input("Enter the value of heigth :"))
# w = int(input("Enter the value of width :"))

reactangle1 = Rectange(4, 3)
reactangle1 = Rectange(2, 3)
reactangle1 = Rectange(2, 5)

# reactangle1.set_dimensions(h, w)
# print(reactangle1.area())
# print(reactangle1.perimeter())
