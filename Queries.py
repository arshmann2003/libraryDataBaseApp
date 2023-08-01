import sqlite3
from UserInput import UserInput as ui


def getData(cursor, table):
    query = f"SELECT * FROM {table}"
    cursor.execute(query)
    result = cursor.fetchall()
    ui.printData(result, table)

def findItemInLibrary(cursor):  
    column_to_check = "Author"
    column_to_check_two = "Title"
    table_to_check = "Item"
    if(input("Press 1 to display all Items, 0 to search for an Item: ").strip() == "1"):
        getData(cursor, table_to_check)
    else:
        author_value_to_check = ui.getAuthorName()
        title_value_to_check = ui.getTitle()
        query = f"SELECT * FROM Item WHERE {column_to_check} = ? AND {column_to_check_two} = ?"
        cursor.execute(query, (author_value_to_check,title_value_to_check))
        result = cursor.fetchone()
        if result:
            print(f"The Item '{title_value_to_check}' by '{author_value_to_check}' is present  in the library.")
        else:
            print(f"The Item '{title_value_to_check}' by '{author_value_to_check}' is NOT present in the library.")


def borrowItem(cursor):
    # Borrowing(BorrowingID, UserID FK, ItemID FK, BorrowDate, DueDate, Returned) 
    getData(cursor, "Borrowing")

    return ""

def returnBorrowedItem(cursor):
    return ""

def donateItem(cursor):
    return ""

def findEvent(cursor):
    return ""

def registerEvent(cursor):
    return ""

def volunteerForLibrary(cursor):
    return ""

def askHelp(cursor):
    return ""
