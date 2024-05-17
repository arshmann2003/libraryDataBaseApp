import sqlite3
import Menu
import Queries as Q

# jupyter nbconvert --to webpdf --allow-chromium-download libraryDriver.ipynb
# User(UserID, Username, Email, Password, UserType) 
# Item(ItemID, ItemType, Title, Author, Publisher, Availability)
# Borrowing(BorrowingID, UserID FK, ItemID FK, BorrowDate, DueDate, Returned) 
# Event(EventID, EventType, Title, Description, Date, Location, Audience) 
# Attendee(EventID FK, UserID FK) Personnel(PersonnelID, Name, Position) 
# Donation(DonationID, UserID FK, ItemID FK, DonationDate)

conn = sqlite3.connect('./sql/library.db')
cursor = conn.cursor()

class Controller:
    def run():
        with conn:
            menuChoice = -1
            while(True):
                Menu.displaylMenu()
                menuChoice = Menu.getMenuInput()
                if(menuChoice == 0): 
                    break
                quereyList(menuChoice)
        
        conn.commit()
        conn.close()
    

def quereyList(num):
    actions = {
        1: Q.findItemInLibrary,
        2: Q.borrowItem,
        3: Q.returnBorrowedItem,
        4: Q.donateItem,
        5: Q.findEvent,
        6: Q.registerEvent,
        7: Q.volunteerForLibrary,
        8: Q.askHelp,
        9: Q.displayData
    }

    action = actions.get(num)
    if action:
        action(cursor)
    else:
        print("Invalid selection, please choose a number between 1 and 9.")
