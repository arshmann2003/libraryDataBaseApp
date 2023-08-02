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
    if(num == 1):
        Q.findItemInLibrary(cursor)
    elif(num == 2):
        Q.borrowItem(cursor)
    elif(num == 3):
        Q.returnBorrowedItem(cursor)
    elif(num == 4):
        Q.donateItem(cursor)
    elif(num == 5):
        Q.findEvent(cursor)
    elif(num == 6):
        Q.registerEvent(cursor)
    elif(num == 7):
        Q.volunteerForLibrary(cursor)
    elif(num == 8):
        Q.askHelp(cursor)    
    elif(num == 9):
        Q.displayData(cursor)


