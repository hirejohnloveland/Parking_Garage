import parking_garage
import user_interface
import time


# Instantiate parking garage and pass it to the UI constructor
number_of_spaces = 5
my_garage = parking_garage.Parking_Garage(number_of_spaces)
user_interface.User_Interface(my_garage)
