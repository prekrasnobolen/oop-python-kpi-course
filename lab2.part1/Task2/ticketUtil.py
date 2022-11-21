import datetime
import json
from ticket import Ticket, StudentTicket, AdvancedTicket, LateTicket


class TicketUtil:

    """
    TicketUtil is used by managing one event.
    Manager sets maximum number of tickets to be sold, date of event, start price of ticket, directory of json file.
    Directory is set default.
    Date should be set in ISO format.
    For safely using files, file is set by name(directory).

    Ticket has a format: ST0003, RT00000004 etc.
        first char means student or regular etc.
        second char just means 'ticket'
        number of digits depends on maximum number of tickets to be sold
            Example: 5000 tickets to be sold, student ticket looks like ST0001
    """

    def __init__(self, maximum, date, price, filename="tickets.json"):
        self.count = 0
        self.maximum = maximum
        self.date = date
        self.price = price
        self.filename = filename
        self.jsonf = filename

    @property
    def jsonf(self):
        return self._jsonf

    @jsonf.setter
    def jsonf(self, streamname):
        if not isinstance(streamname, str):
            raise TypeError("To use file safely, set filename as parameter")
        try:
            self._jsonf = open(streamname, "r")
            check = json.load(self.jsonf)
        except FileNotFoundError:
            self._jsonf = open(streamname, "w")
            json.dump({"tickets": []}, self.jsonf, indent=4)
        except json.decoder.JSONDecodeError:
            self._jsonf = open(streamname, "w")
            json.dump({"tickets": []}, self.jsonf, indent=4)
        else:
            if "tickets" in check:
                for ticket in check["tickets"]:
                    if len(ticket) != 2:
                        raise TypeError("Ticket should have only code and price")
                    if "code" and "price" in ticket:
                        if not isinstance(ticket["code"], str):
                            raise TypeError("Code should be string")
                        if not isinstance(ticket["price"], (float, int)):
                            raise TypeError("Price of ticket should be a number")
        finally:
            self.jsonf.close()

    @property
    def maximum(self):
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        if not isinstance(maximum, int):
            raise TypeError
        if maximum < 0:
            raise ValueError
        self._maximum = maximum

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, count):
        self._count = count

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if not isinstance(price, (float, int)):
            raise TypeError
        self._price = price

    @property
    def date(self):
        return self._eventDate

    @date.setter
    def date(self, date):
        self._eventDate = datetime.datetime.fromisoformat(date)

    def save_ticket(self, ticket):
        try:
            self._jsonf = open("tickets.json", "r")
        except FileNotFoundError:
            raise FileNotFoundError("File not found")
        data = json.load(self.jsonf)
        self.jsonf.close()
        self._jsonf = open("tickets.json", "w")
        data["tickets"].append(ticket.jsonformat())
        json.dump(data, self.jsonf, indent=4)
        self._jsonf.close()

    def add_ticket(self, customer="common"):
        self.count += 1

        if self.count + 1 > self.maximum:
            return ValueError("All tickets are sold")
        if customer != "common" and customer != "student":
            raise ValueError("Customer should be 'student' or 'common'")
        difference = self.date - datetime.datetime.now()

        coder = f"{self.count}".zfill(len(str(self.maximum)))

        if customer == "student":
            ticket = StudentTicket(f"ST{coder}", self.price)
        elif difference.days >= 60:
            ticket = AdvancedTicket(f"AT{coder}", self.price)
        elif difference.days <= 10:
            ticket = LateTicket(f"LT{coder}", self.price)
        else:
            ticket = Ticket(f"RT{coder}", self.price)

        self.save_ticket(ticket)
        return ticket

    def get_ticket(self, code):
        # by code
        try:
            self._jsonf = open("tickets.json", "r")
        except FileNotFoundError:
            raise FileNotFoundError
        data = json.load(self.jsonf)
        for ticket in data["tickets"]:
            if ticket["code"] == code:
                return Ticket(ticket["code"], ticket["price"])
        return None

