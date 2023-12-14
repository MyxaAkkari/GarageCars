import os
import json
from icecream import ic

def clearScreen():
    """Clears the terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

cars = []
MY_DATA = 'garage.txt'

def load_data():
    global cars
    with open(MY_DATA, 'r') as filehandle:
        cars = json.load(filehandle)

def save_2_file():
    with open(MY_DATA, 'w') as filehandle:
        json.dump(cars, filehandle)

def menu():
    """Prints the menu, returns user selection."""
    ic('V -> View all cars.')
    ic('A -> Add a new car.')
    ic('E -> Edit a car.')
    ic('D -> Delete a car.')
    ic('Q -> Quit program.')
    return input('What would you like to do?: ').lower()

def menuAction(selection):
    """Decides what to do with user selection."""
    if selection == 'v': printcars()
    elif selection == 'a': 
        addCar()
    elif selection == 'd': 
        delCar() 
        ic("Car deleted!")
    elif selection == 'e': editCar()
    elif selection == 'q': 
        save_2_file()
        ic("Bye Bye!")
        exit()

def addCar():
    """Add a car to the file."""
    cars.append({"brand":input("Car Brand: "), "model":input("Car model: "), "color":input("Car color: ")})
    ic("Car added.")

def printcars():
    """Prints current cars in list with index/number."""
    #Thanks Amir xD
    number = 0
    for obj in cars:
        ic("----------------")
        ic(number)
        ic(obj['brand'])
        ic(obj['model'])
        ic(obj['color'])
        number += 1

def delCar():
    """Delete a car by using its index in list."""
    printcars()
    carNum = int(input("Car Number?: "))
    cars.pop(carNum)

def editCar():
    """Edit a car, delete's old entry and adds a new one."""
    printcars()
    carNum = int(input('Which car would you like to modify? Car number: '))
    cars.pop(carNum)
    addCar()
    

def main():
    clearScreen()
    load_data()
    while True:
        userSelection = menu()
        clearScreen()
        menuAction(userSelection)




if __name__ == "__main__":
    main()

