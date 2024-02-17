class Rectange:

    def set_dimensions(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)


reactangle1 = Rectange()

h = int(input("Enter the value of heigth :"))
w = int(input("Enter the value of width :"))
reactangle1.set_dimensions(h, w)
print(reactangle1.area())
print(reactangle1.perimeter())
