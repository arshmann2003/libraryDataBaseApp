
import time

menuList = {1:"Find an item in the library",2:"Borrow an item from the library",3:"Return a borrowed item",4:"Donate an item to the library", 5:"Find an event in the library",6:"Register for an event in the library",7:"Volunteer for the library", 8:"Ask for help from a librarian",9:"Display all table data"}

def displaylMenu():
    n = len(menuList)
    print(f"\n=============== MENU =================")
    for i in range(n):
     
        print(f"{i+1}. {menuList[i+1]}")
    print(f"=======================================")

def getMenuInput():
    while(True):
        userInput = input(f"Choose Menu Option(1-9) or 0 to quit: ")
        if(validateInput(userInput)):
            return int(userInput)
    
def validateInput(userInput):
    if(userInput.isdigit()):
        num = int(userInput)
        return num >= 0 and num <= 9
    return False
