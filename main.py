import parking_garage


def UserInterface(this_garage):
    while True:
        print("Please choose from the following options")
        print("1 - Park")
        print("2 - Pay for Parking")
        print("3 - Exit Garage")
        print("4 - Quit Program")
        response = input("Please enter the number of your selection: ")
        if response == "1":
            this_garage.take_Ticket()
        elif response == "2":
            this_garage.leave_Garage()
        elif response == "3":
            this_garage.leave_Garage()
        elif response == "4":
            print("Program exit")
            break
        else:
            print("Invalid Input Entered - Please try again")
            continue


this_garage = parking_garage.Parking_Garage()
UserInterface(this_garage)
