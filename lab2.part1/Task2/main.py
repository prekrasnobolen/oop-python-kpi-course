from ticketUtil import TicketUtil

if __name__ == "__main__":
    tester = TicketUtil(300, "2022-12-31", 5)
    tester.add_ticket()
    tester.add_ticket()
    tester.add_ticket()
    print(tester.get_ticket("RT002"))
