import parking_garage
import os
import time

banner = """
##############################################
            PARKING GARAGE - WELCOME
##############################################"""


def cls():
    """Function to clear the console"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():
    """Print header at mainscreen"""
    cls()
    print(banner)
    t = time.localtime()
    print(time.strftime("%b %d %Y %H:%M:%S", t))
    print()


def UserInterface(this_garage):
    """User interface for console app"""
    while True:
        print_header()
        print("Please choose from the following options")
        print("1 - Park")
        print("2 - Pay for Parking")
        print("3 - Exit Garage")
        print("4 - Quit Program")
        print("5 - Admin")
        response = input("Please enter the number of your selection: ")

        cls()
        if response == "1":
            this_garage.take_Ticket()
        elif response == "2":
            this_garage.pay_For_Parking()
        elif response == "3":
            this_garage.leave_Garage()
        elif response == "4":
            print("Program exit")
            break
        elif response == "5":
            this_garage.admin_report()
        else:
            print("Invalid Input Entered - Please try again")
            continue


print_header()
UserInterface(this_garage := parking_garage.Parking_Garage())
