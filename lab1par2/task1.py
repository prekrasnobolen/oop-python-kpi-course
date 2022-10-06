class Rectangle:
    def __init__(self):
        self.height = 1
        self.width = 1

    def setHeight(self, value):
        if isinstance(value, float):
            if 0.0 <= value <= 20.0:
                self.height = value
                return True
            else:
                raise ValueError("Value Error")
        else:
            raise TypeError("TypeError")

    def getHeight(self):
        return self.height

    def setWidth(self, value):
        if isinstance(value, float):
            if 0.0 <= value <= 20.0:
                self.width = value
                return True
            else:
                raise ValueError("Value Error")
        else:
            raise TypeError("TypeError")


    def getWidth(self):
        return self.width

    def area(self):
        return self.height * self.width

    def perimetr(self):
        return 2*(self.height + self.width)


tester = Rectangle()
print(f"Perimetr is {tester.perimetr()}")
print(f"Area is {tester.area()}")
