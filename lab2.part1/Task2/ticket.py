class Ticket:
    def __init__(self, code, price):
        self._code = code
        self._price = price

    def __str__(self):
        return f"Ticket: {self.code}, price: {self.price}"

    def jsonformat(self):
        return {
            "code": self.code,
            "price": self.price
        }

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        if not isinstance(code, str):
            raise TypeError
        self._code = code

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if not isinstance(price, (float, int)):
            raise TypeError
        if price < 0:
            raise ValueError
        self._price = price


class AdvancedTicket(Ticket):

    def __init__(self, code, price, multi=0.6):
        super().__init__(code, price*multi)


class LateTicket(Ticket):

    def __init__(self, code, price, multi=1.1):
        super().__init__(code, price*multi)


class StudentTicket(Ticket):

    def __init__(self, code, price, multi=0.5):
        super().__init__(code, price*multi)


x = Ticket("iu3h", True)


