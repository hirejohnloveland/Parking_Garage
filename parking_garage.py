class Parking_Garage():
    def __.init__(self):
        self.tickets = 0  # tickets sold
        self.total_spaces = 20  # total number of spaces in garage
        self.parking_spaces = {}  # Initialize a dictionary of parking spaces
        for number in range(20):  # Assign each parking slot a status of "Open on startup"
            parking_spaces[number] = "Open"
        # Initialize a dictionary tracking whether tickets are paid or not
        self.ticket_status = {}


def take_Ticket(self):
    pass
# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True


def leave_Garage(self):
    pass
# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)


def pay_For_Parking(self):
    pass
    # - payForParking
    # - Display an input that waits for an amount from the user and store it in a variable
    # - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
    # - This should update the "currentTicket" dictionary key "paid" to True


this_garage = Parking_Garage()


def main_loop()


while True:
    x = input(x):
        if x = "":
            this_garage.pay_For_Parking()
        elif x = "":
            this_garage.take_Ticket()
        elif x = "":
            this_garage.leave_Garage()
        else:
            print("Garage closing exit")
