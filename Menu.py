menuList = {1:"Find an item in the library",2:"Borrow an item from the library",3:"Return a borrowed item",4:"Donate an item to the library", 5:"Find an event in the library",6:"Register for an event in the library",7:"Volunteer for the library", 8:"Ask for help from a librarian"}

def displaylMenu():
    n = len(menuList)
    for i in range(n):
        print(str(i+1) + " " + menuList[i+1])

def getInput():
    while(True):
        userInput = input("Choose Menu Option(1-8) or 0 to quit: ")
        if(validateInput(userInput)):
            print("\n")
            return int(userInput)
    
def validateInput(userInput):
    if(userInput.isdigit()):
        num = int(userInput)
        return num >= 0 and num <= 8
    return False
