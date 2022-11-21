from PizzaOrder import PizzaOrder

if __name__ == "__main__":
    newOrder = PizzaOrder()
    newOrder.order_pizza("peperoni", "black olives")
    newOrder.order_pizza("mozzarella")
    print(newOrder)
    anotherOrder = PizzaOrder()
    anotherOrder.order_pizza("chicken", "tomatoes", "verdure")
    print(anotherOrder)