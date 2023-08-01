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

conn = sqlite3.connect('library.db')
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


def quereyList(num):
    match num:
        case 1:
            Q.findItemInLibrary(cursor)
        case 2:
            Q.borrowItem(cursor)
        case 3:
            Q.returnBorrowedItem(cursor)
        case 4:
            Q.donateItem(cursor)
        case 5:
            Q.findEvent(cursor)
        case 6:
            Q.registerEvent(cursor)
        case 7:
            Q.volunteerForLibrary(cursor)
        case 8:
            Q.askHelp(cursor)    

