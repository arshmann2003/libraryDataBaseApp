import sqlite3
import Menu
import Queries as Q

QuereyList = {1:Q.findItemInLibrary(),2:Q.borrowItem(),3:Q.returnBorrowedItem(),4:Q.donateItem(),5:Q.findEvent(),6:Q.registerEvent(),7:Q.volunteerForLibrary(),8:Q.askHelp()}

conn = sqlite3.connect('library.db')

cursor = conn.cursor()
print("Opened database successfully \n")

with conn:
    menuChoice = -1
    while(True):
        Menu.displaylMenu()
        menuChoice = Menu.getInput()
        if(menuChoice == 0): 
            break

        querey = QuereyList[menuChoice]
        print(querey)
  
    