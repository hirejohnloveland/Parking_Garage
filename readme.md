# Parking Garage Projectd  

#### Project Description
This project is a simple Python teaching project for managing a parking garage, featuring an object oriented design with a loosely coupled architecture.  

## main.py
This is the entry point for the program, the user instantiates a garage object with a finite number of spaces and passes it to the UI

## user_interface.py
The interface is responsible for displaying the interface, and receiving all input.

## parking_garage.py
The parking garage module contains all of the logic for the operation of the garage, it is entirely decoupled from the UI, making it easy to create an alternate UI, such as a web interface.  It features three public methods and several properties to track the current state of the garage, and a variety of self-commenting private methods to aide in code readability and re-use.
