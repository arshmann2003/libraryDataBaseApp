import sqlite3
import Menu
import Queries as Q

QuereyList = {1:Q.findItemInLibrary()}

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
  
    