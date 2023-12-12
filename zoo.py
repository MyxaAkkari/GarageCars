import os
import json

def clearScreen():
    """Clears the terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

animals = []
MY_DATA = 'zoo.txt'

def load_data():
    global animals
    with open(MY_DATA, 'r') as filehandle:
        animals = json.load(filehandle)

def save_2_file():
    with open(MY_DATA, 'w') as filehandle:
        json.dump(animals, filehandle)

def menu():
    """Prints the menu, returns user selection."""
    print('V -> View all animals.')
    print('A -> Add a new animal.')
    print('E -> Edit an animal.')
    print('D -> Delete an animal.')
    print('Q -> Quit program.')
    return input('What would you like to do?: ').lower()

def menuAction(selection):
    """Decides what to do with user selection."""
    if selection == 'v': printanimals()
    elif selection == 'a': 
        addAnimal()
    elif selection == 'd': 
        delAnimal() 
        print("Animal deleted!")
    elif selection == 'e': editAnimal()
    elif selection == 'q': 
        save_2_file()
        print("Bye Bye!")
        exit()

def addAnimal():
    """Add a Animal to the file."""
    animals.append({"name":input("Animal name: "), "species":input("Animal Species: "), "age":input("Animal age: ")})
    print("Animal added.")

def printanimals():
    """Prints current animals in list with index/number."""
    #Thanks Amir xD
    i = 0
    for obj in animals:
        print("----------------")
        print(f"Number: {str(i)}")
        print(f"Name: {obj['name']}")
        print(f"Species: {obj['species']}")
        print(f"Age: {obj['age']}")
        i += 1

def delAnimal():
    """Delete a Animal by using its index in list."""
    printanimals()
    AnimalNum = int(input("Animal Number?: "))
    animals.pop(AnimalNum)

def editAnimal():
    """Edit a Animal, delete's old entry and adds a new one."""
    printanimals()
    AnimalNum = int(input('Which Animal would you like to modify? Animal number: '))
    animals.pop(AnimalNum)
    addAnimal()
    

def main():
    clearScreen()
    load_data()
    while True:
        userSelection = menu()
        clearScreen()
        menuAction(userSelection)




if __name__ == "__main__":
    main()

