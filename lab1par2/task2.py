def find_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if greater % x == 0 and greater % y == 0:
            res = greater
            break
        greater += 1
    return res


class Rational:
    def __init__(self, numerator, denominator):
        if isinstance(numerator, int):
            if isinstance(denominator, int):
                if denominator != 0:
                    i = 2
                    while True:
                        if i > denominator/2:
                            break
                        if denominator % i == 0 and numerator % i == 0:
                            numerator /= i
                            denominator /= i
                            i -= 1
                        i += 1
                    self.numerator = numerator
                    self.denominator = denominator
                else:
                    raise ZeroDivisionError("ZeroDivisionError")
            else:
                raise TypeError("Denominator : type error")
        else:
            raise TypeError("Numerator type error")

    def get_num(self):
        return self.numerator

    def get_dom(self):
        return self.denominator

    def __add__(self, other):
        lcm = find_lcm(self.denominator, other.get_dom())
        firstNum = self.numerator * (lcm/self.numerator)
        secondNum = other.get_dom() * (lcm/other.get_dom)
        resNum = firstNum + secondNum
        return Rational(resNum, lcm)

    def __mul__(self, other):
        resNum = self.numerator * other.get_num()
        resDom = self.denominator * other.get_dom()
        return Rational(resNum, resDom)

    def __sub__(self, other):
        lcm = find_lcm(self.denominator, other.get_dom())
        firstNum = self.numerator * (lcm / self.numerator)
        secondNum = other.get_dom() * (lcm / other.get_dom)
        resNum = firstNum - secondNum
        return Rational(resNum, lcm)

    def __truediv__(self, other):
        resNum = self.numerator * other.get_dom()
        resDom = self.denominator * other.get_num()
        return Rational(resNum, resDom)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def show(self):
        print(f"{self.numerator}/{self.denominator}")

    def show_float(self):
        print(self.numerator/self.denominator)


first = Rational(5, 7)
second = Rational(3, 4)

print(f"{first} * {second} = {first.__mul__(second)}")