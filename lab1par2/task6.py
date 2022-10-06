class Node:
    def __init__(self, code, price, number=1):
        if isinstance(price, float) and price > 0:
            self.number = number
            self.code = code
            self.price = price
            self.right = None
            self.prev = None
        else:
            raise TypeError("Price is a number")

    def __str__(self):
        return f"{self.code} : {self.price}"

    def get_next(self):
        return self.right

    def get_prev(self):
        return self.prev

    def set_price(self, price):
        self.price = price

    def get_price(self, price):
        return self.price

    def get_code(self):
        return self.code


class BinaryTry:
    def __int__(self):
        self.root = None

    def add_node(self, code, price):
        if self.root:
            current = self.root
            while True:
                if code >= current.get_code():
                    if current.code == code:
                        current.number += 1
                    elif current.right:
                        current = current.right
                    else:
                        current.right = Node(code, price)
                        break
                else:
                    if current.right:
                        current = current.left
                    else:
                        current.left = Node(code, price)
                        break
    def find_cost(self, code):
        current = self.root
        while True:
            if code >= current.get_code():
                print("ok")

    def findcost(self, code, current=None):
        if not current:
            current = self.root
        if current.code == code:
            return current.number * current.price
        if current.right:
            return self.findcost(code, current.right)
        if current.left:
            return self.findcost(code, current.left)







