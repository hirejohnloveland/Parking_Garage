class Parking_Garage():
    # Initialize the Parking Garage object in a valid state (no tickets issued, no tickets paid, no spaces used)
    # Public Methods for UI access allow users to park, pay, and exit.  Additionally there is an admin report which allow the
    # operator (or developer) to generate a printout of the tickets sold, tickets paid / unpaid, and a list of the currently
    # avaible and taken parking spaces.  Multiple private methods below assist the public methods and promote clean coding

    def __init__(self, num_spaces):
        """Create a new parking garage with a given number of parking spaces available"""
        self.tickets = 0  # number of tickets issued
        self.payment_status = {}  # Dict of tickets - T- paid, F - unpaid
        self.parking_spaces = {}  # Dict of parking spaces
        for number in range(1, num_spaces + 1):
            self.parking_spaces[number] = "Open"  # Initialize empty garage.

    ##############################################
    ###### Public Methods ########################
    ##############################################

    def take_Ticket(self):
        """Issues a ticket number and the next available parking space to user if the lot isn't full"""
        if self.__lot_full():
            return "The lot is full please return once someone leaves"
        else:
            ticket_number = self.__issue_ticket()
            current_space = self.__next_free_space()
            self.parking_spaces[current_space] = ticket_number
            self.payment_status[ticket_number] = False
            return f"You have ticket number {ticket_number} for parking space number {current_space}. Please pay the attendent before exiting"

    def pay_For_Parking(self, ticket_number):
        """Validates the user's ticket number is a valid, UNPAID ticket, then accepts payment and marks it in paid in the payment_status dictionary"""
        if not self.__ticket_valid(ticket_number):
            return "Please enter a valid ticket number!"
        if self.__ticket_paid(ticket_number):
            return "This ticket is already paid. Please exit the parking garage"
        else:
            self.payment_status[ticket_number] = True
            return "Thank you for your payment, please exit the parking garage"

    def leave_Garage(self, ticket_number):
        """Validates the user's ticket number is a valid, PAID ticket, then marks the space open in the parking_spaces dictionary and allows the user to exit"""
        if not self.__ticket_valid(ticket_number):
            return "Please enter a valid ticket number!"
        if not self.__ticket_paid(ticket_number):
            return "This ticket is not paid, please pay before leaving"
        else:
            self.parking_spaces[self.__find_ticketspace(
                ticket_number)] = "Open"
            return "Thank you for your business, have a nice day"

    def admin_report(self):
        """Analytical Report for Garage Owner (Or developer that wants to see what the code is doing easily)"""
        return """{} tickets have been sold") 
                \nTicket payment status: \n{} 
                \nList of the lot spaces and associated tickets: 
                \n{}\n""".format(self.tickets, self.payment_status, self.parking_spaces)

    ##############################################
    ###### Private Methods #######################
    ##############################################

    def __issue_ticket(self):
        self.tickets += 1
        return self.tickets

    def __lot_full(self):
        """Boolean check if garage contains open spaces"""
        for spaces in self.parking_spaces.values():
            if spaces == "Open":
                return False
        return True

    def __next_free_space(self):
        """Finds the first available parking space in the dictionary"""
        for parking_spot, occupied in self.parking_spaces.items():
            if occupied == "Open":
                return parking_spot

    def __ticket_valid(self, ticket_number):
        """Boolean check if ticket is in ticket dictionary"""
        return (ticket_number) in self.parking_spaces.values()

    def __ticket_paid(self, ticket_number):
        """Boolean check if ticked is paid or unpaid"""
        return self.payment_status[(ticket_number)]

    def __find_ticketspace(self, ticket_number):
        """finds the parking spot associated with a given ticket"""
        for parking_spot, occupied in self.parking_spaces.items():
            if occupied == ticket_number:
                return parking_spot
