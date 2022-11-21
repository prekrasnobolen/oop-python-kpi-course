all_pizzas = {}


def pizza_register(cls):
    all_pizzas[cls.name] = cls
    return cls


def retrieve_extras(filename="extras.txt"):     # extras to pizza are set with file
    dic = {}
    with open(filename, "r") as file:
        for line in file:
            key, value = line.split(':')

            dic[key] = float(value)
        return dic


def retrieve_pizzas(filename="pizzas.txt"):     # pizzas are set with file
    dic = {}
    with open(filename, "r") as file:
        for line in file:
            key, value = line.split(':')
            dic[int(key)] = value.strip()
        return dic


class Pizza:
    """

    """
    name = ""
    ingredients = []
    _extras_dict = retrieve_extras("extras.txt")

    def __init__(self, extras):
        self.extras = extras
        self._price = 0
        for ingredient in self.ingredients:
            price_buff = self._extras_dict.get(ingredient)
            if price_buff:
                self._price += price_buff
            else:
                raise ValueError(f"There is no such ingredient as '{ingredient}'")

        self._price += sum(self.extras.values())

    @property
    def extras(self):
        return self._extras

    @property
    def price(self):
        return self._price

    @extras.setter
    def extras(self, extras):
        self._extras = {}
        for extra in extras:
            if extra in self._extras_dict.keys():
                updater = {extra: self._extras_dict[extra]}
                self._extras.update(updater)
            else:
                raise ValueError(f"There is no such extra as '{extra}'")

    def __str__(self):
        pizza = f"Pizza {self.name} -- {self.price:.2f}\n"
        if self.extras.keys():
            pizza += "Extras: " + ", ".join(self.extras.keys()) + '\n'
        return pizza


@pizza_register
class Margarita(Pizza):
    name = "Margarita"
    ingredients = ["base", "cheese", "basilic"]

    def __init__(self, extras):
        super().__init__(extras)


@pizza_register
class QuadroFormaggi(Pizza):
    name = "Quadro formaggi"
    ingredients = ["base", "cheese", "mozzarella", "cheddar", "parmigiano", "basilic", "dor blue"]

    def __init__(self, extras):
        super().__init__(extras)


@pizza_register
class Capricciosa(Pizza):
    name = "Capricciosa"
    ingredients = ["base", "cheese", "mushrooms", "peperoni"]

    def __init__(self, extras):
        super().__init__(extras)


@pizza_register
class Hawaiian(Pizza):
    name = "Hawaiian"
    ingredients = ["base", "cheese", "mozarella", "chicken", "ananas"]

    def __init__(self, extras):
        super().__init__(extras)


@pizza_register
class Calzone(Pizza):
    name = "Calzone"
    ingredients = ["base", "cheese", "mushrooms", "peperoni", "cheddar"]

    def __init__(self, extras):
        super().__init__(extras)


@pizza_register
class Bavarian(Pizza):
    name = "Bavarian"
    ingredients = ["base", "cheese", "mozzarella", "sausages", "verdure", "tomatoes", "mushrooms"]

    def __init__(self, extras):
        super().__init__(extras)


@pizza_register
class Ukrainian(Pizza):
    name = "Ukrainian"
    ingredients = ["base", "cheese", "chicken", "peperoni", "verdure"]

    def __init__(self, extras):
        super().__init__(extras)
