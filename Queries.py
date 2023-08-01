import sqlite3
from UserInput import UserInput as ui

def findItemInLibrary(cursor):

    value_to_check = ui.getAuthorName()
    column_to_check = "Author"
    column_to_check_two = "Title"
    bookTitle = "To Kill a Mockingbird"
    table_to_check = "Item"

    query = f"SELECT * FROM {table_to_check} WHERE {column_to_check} = ? AND {column_to_check_two} = ?"
    cursor.execute(query, (value_to_check,bookTitle))

    # Fetch the result (if any)
    result = cursor.fetchone()

    # Check if the value exists
    if result:
        print(f"The value '{value_to_check}' is present in the '{column_to_check}' column of the '{table_to_check}' table.")
    else:
        print(f"The value '{value_to_check}' is NOT present in the '{column_to_check}' column of the '{table_to_check}' table.")


def borrowItem(cursor):
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
