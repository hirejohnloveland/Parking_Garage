class Parking_Garage():
    # Initialize the Parking Garage object in a valid state (no tickets issued, no tickets paid, no spaces used)
    def __init__(self):
        # .tickets counts the number of tickets issued,
        # .ticket_status tracks whether issued tickets are paid or not with a T/F
        self.tickets = 0
        self.ticket_status = {}

        # Set the number of spaces in the garage and initialize a dictionary of parking spots.  Each spot starts with "Open"
        # until a ticket number is assigned to the slot.
        self.TOTAL_SPACES = 20
        self.parking_spaces = {}
        for number in range(1, self.TOTAL_SPACES+1):
            self.parking_spaces[number] = "Open"

    def take_Ticket(self):
        """Issues a ticket number and the next available parking space to user if the lot isn't full"""

        if self.lot_full():
            print("The lot is full please return once someone leaves")
            input('Press any key to continue...')
            return
        else:
            self.tickets += 1
            current_space = self.next_free_space()
            self.parking_spaces[current_space] = self.tickets
            self.ticket_status[self.tickets] = False
        print(
            f"You have ticket number {self.tickets} for parking space number {current_space}. Please pay the attendent before exiting")
        input('Press any key to continue...')

    def pay_For_Parking(self):
        """Validates the user's ticket number is a valid, UNPAID ticket, then accepts payment and marks it in paid in the ticket_status dictionary"""
        ticket_number = input("Please enter your ticket number: ")
        try:
            ticket_number = int(ticket_number)
        except:
            print("Please enter an integer for this field. Returning to main menu!")
            input('Press any key to continue...')
            return
        if not self.ticket_valid(ticket_number):
            print("Please enter a valid ticket number!")
            input('Press any key to continue...')
            return
        if self.ticket_paid(ticket_number):
            print("This ticket is already paid. Please exit the parking garage")
            input('Press any key to continue...')
            return
        else:
            print("Thank you for your payment, please exit the parking garage")
            self.ticket_status[ticket_number] = True
            input('Press any key to continue...')

    def leave_Garage(self):
        """Validates the user's ticket number is a valid, PAID ticket, then marks the space open in the parking_spaces dictionary and allows the user to exit"""
        ticket_number = input("Please enter your ticket number: ")
        try:
            ticket_number = int(ticket_number)
        except:
            print("Please enter an integer for this field. Returning to main menu!")
            input('Press any key to continue...')
            return
        if not self.ticket_valid(ticket_number):
            print("Please enter a valid ticket number!")
            input('Press any key to continue...')
            return
        if not self.ticket_paid(ticket_number):
            print("This ticket is not paid, please pay before leaving")
            input('Press any key to continue...')
            return
        else:
            print("Thank you for your business, have a nice day")
            current_space = self.find_ticketspace(ticket_number)
            self.parking_spaces[current_space] = "Open"
            input('Press any key to continue...')

    def admin_report(self):
        # Analytical Report for Garage Owner (Or developer that wants to see what the code is doing easily) #
        print(f"{self.tickets} tickets have been sold")
        print("Ticket List:")
        print(self.ticket_status)
        print("List of the lot spaces:")
        print(self.parking_spaces)
        input('Press any key to continue...')

    # These Helper methods assist the take_ticket method to validate the lot is full
    # and provide the next free parking space from the parking_spaces dictionary

    def lot_full(self):
        """Boolean check if garage contains open spaces"""
        for spaces in self.parking_spaces.values():
            if spaces == "Open":
                return False
        return True

    def next_free_space(self):
        """finds the first available parking space in the dictionary"""
        for parking_spot, occupied in self.parking_spaces.items():
            if occupied == "Open":
                return parking_spot

    # These helper methods validate that the ticket is legit and paid for the leave_garage
    # and pay_for_parking methods

    def find_ticketspace(self, input_ticket):
        """finds the parking spot associated with a given ticket"""
        for parking_spot, occupied in self.parking_spaces.items():
            if occupied == input_ticket:
                return parking_spot

    def ticket_valid(self, input_ticket):
        """Boolean check if ticket is in ticket dictionary"""
        return (input_ticket) in self.parking_spaces.values()

    def ticket_paid(self, input_ticket):
        """Boolean check if ticked is paid or unpaid"""
        return self.ticket_status[(input_ticket)]
