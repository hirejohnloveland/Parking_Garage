import time
import os
import time


class User_Interface():
    # UI class receives a parking_garage object and instantiates a UI on the console with a header
    # and current date/time.  UI is cleared after each iteration via the os package / clear_console() UDF.  Current
    # time is displayed via the time package / get_current_time UDF.  Loop continues until user exit."""

    def __init__(self, parking_garage):
        self.parking_garage = parking_garage
        self.print_header()
        self.ui_launch()

    # Main UI Loop

    def ui_launch(self):
        """User interface for console app"""
        while True:
            self.print_header()
            print("Please choose from the following options")
            print("1 - Park")
            print("2 - Pay for Parking")
            print("3 - Exit Garage")
            print("4 - Quit Program")
            print("5 - Admin")
            response = input("Please enter the number of your selection: ")

            self.clear_console()
            if response == "1":
                self.parking_garage.take_Ticket()
            elif response == "2":
                self.parking_garage.pay_For_Parking()
            elif response == "3":
                self.parking_garage.leave_Garage()
            elif response == "4":
                print("Program exit")
                break
            elif response == "5":
                self.parking_garage.admin_report()
            else:
                print("Invalid Input Entered - Please try again")
                continue

    # Helper functions to manage the console

    def print_header(self):
        """Print header at mainscreen"""
        self.clear_console()
        print(self.get_banner_image())
        print(self.get_current_time())
        print()

    def clear_console(self):
        """Function to clear the console"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_banner_image(self):
        """Function to display the banner image"""
        return """
##############################################
            PARKING GARAGE - WELCOME
##############################################"""

    def get_current_time(self):
        """Function to return the current time"""
        return (time.strftime("%b %d %Y %H:%M:%S", t := time.localtime()))
