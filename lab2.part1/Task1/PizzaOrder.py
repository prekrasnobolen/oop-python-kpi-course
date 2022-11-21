from datetime import datetime
import Pizza


class PizzaOrder:
    _orders = 0
    _day_pizza_dict = Pizza.retrieve_pizzas()

    def __init__(self):
        self._day = datetime.weekday(datetime.now()) + 1
        PizzaOrder._orders += 1
        self._code = f"{self._orders}".zfill(3)
        self._pizzas = []

    @property
    def code(self):
        return self._code

    @property
    def day(self):
        return self._day

    @property
    def pizzas(self):
        return self._pizzas

    def total(self):
        total = 0
        for pizza in self.pizzas:
            total += pizza.price
        return total

    def __str__(self):
        order = f"Order:{self.code}\n"
        i = 1
        for pizza in self.pizzas:
            order += f"{i}. {pizza}"
            i += 1
        order += f"\nTotal price: {self.total():.2f}€"
        return order

    def order_pizza(self, *extras):
        pizza = Pizza.all_pizzas[self._day_pizza_dict[self.day]]
        order = pizza(extras)
        self._pizzas.append(order)
        return order
