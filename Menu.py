from colorama import Fore, Style

menuList = {1:"Find an item in the library",2:"Borrow an item from the library",3:"Return a borrowed item",4:"Donate an item to the library", 5:"Find an event in the library",6:"Register for an event in the library",7:"Volunteer for the library", 8:"Ask for help from a librarian"}

def displaylMenu():
    n = len(menuList)
    print(f"{Fore.BLUE}\n=============== MENU ================={Style.RESET_ALL}")
    for i in range(n):
        print(f"{Fore.GREEN}{i}. {menuList[i+1]}{Style.RESET_ALL}")
    print(f"{Fore.BLUE}======================================={Style.RESET_ALL}")

def getInput():
    while(True):
        userInput = input(f"{Fore.RED}Choose Menu Option(1-8) or 0 to quit: ")
        {Style.RESET_ALL}
        if(validateInput(userInput)):
            return int(userInput)
    
def validateInput(userInput):
    if(userInput.isdigit()):
        num = int(userInput)
        return num >= 0 and num <= 8
    return False
