class Product:
    def __init__(self, price, description, dimension):
        if isinstance(price, float) :
            if price > 0:
                self.price = price
            else:
                raise ValueError("Price : Value error")
        else:
            raise TypeError("Type error ")
        if isinstance(dimension, float):
            if dimension > 0:
                self.dimension = dimension
            else:
                raise ValueError("Dimension : Value error")
        else:
            raise TypeError("Dimension : Type error")
        self.description = description

        self.next = None  # Product is a node of singly linked list

    def __str__(self):
        return f"| {self.description:14} | {self.price:7} | {self.dimension:5} |"

    def getPrice(self):
        return self.price


class Customer:
    def __init__(self, surname, name, patronymic, phone):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone = phone

    def show(self):
        print(f"Customer: {self.surname} {self.name} {self.patronymic}")
        print(f"Tel: {self.phone}")


class Order:
    def __init__(self):
        self.customer = None
        self.products = None  # head of singly linked list of products

    def addProduct(self, price, description, dimension):
        if not self.products:
            self.products = Product(price, description, dimension)
        else:
            current = self.products
            while current.next:
                current = current.next
            current.next = Product(price, description, dimension)

    def total(self):
        current = self.products
        total = 0
        while current:
            total += current.getPrice()
            current = current.right
        return total

# useless, just for me
    def show(self):
        self.customer.show()
        print("------------------------------------")
        print("|     Total      |  Price  |  Dim  |")
        current = self.products
        while current:
            print(current)
            current = current.right
        print("------------------------------------")
        print(f"\nTotal price is: {self.total()}")

    # useless, just for me
    def orderUtil(self):
        print("Enter surname:")
        surname = input()
        print("Enter name:")
        name = input()
        print("Enter patronymic")
        patronymic = input()
        print("Enter phone number:")
        phone = input()
        self.customer = Customer(surname, name, patronymic, phone)
        print("Success")
        print("***Products***")
        while True:
            print("Enter description:")
            description = input()
            print("Enter price:")
            price = float(input())
            print("Enter dimension:")
            dimension = float(input())
            self.addProduct(price, description, dimension)
            print("1 - to enter another product\n"
                  "2 - to end the order")
            choice = input()
            if choice == '2':
                self.show()
                break

    def set_customer(self, surname, name, patronymic, phone):
        self.customer = Customer(surname, name, patronymic, phone)



# main


lab = Order()
lab.set_customer("Danylo Konovalenko Viktorovych +380993651469".split())
lab.addProduct(43.5, "Something", 300)
lab.addProduct(12.6, "Anotherthing", 200)
print(lab.total)


