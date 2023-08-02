import sqlite3
from UserInput import UserInput as ui
from datetime import datetime, timedelta

def getData(cursor, table, print):
    query = f"SELECT * FROM {table}"
    cursor.execute(query)
    result = cursor.fetchall()
    if(print):
        ui.printData(result, table)
    return result

def findItemInLibrary(cursor):  
    column_to_check = "Author"
    column_to_check_two = "Title"
    table_to_check = "Item"
    if(input("Press 1 to display all Items, 0 to search for an Item: ").strip() == "1"):
        getData(cursor, table_to_check, True)
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
    # User(UserID, Username, Email, Password, UserType) 
    rows = getData(cursor, "Item", False)
    itemID = ui.getItemID(rows)
    if(itemID == -1): return
    
    if(ui.returningUser()):
        username = ui.getUsername()
        if(username == "-1"):
            return
        
        if(username in getUsernames(cursor)):
            invalid = True 
            while(invalid):
                password = ui.getPassword()
                if(validatePassword(cursor, username, password)):
                    insertIntoBorrowing(cursor, username, itemID)
                    return
                elif(password=="-1"):
                    return
                else:
                    print(f"invalid password for {username}")
        else:
            print("user not found")
    else:
        # createNewUser(cursor)
        getData(cursor, "User", True)

    # getData(cursor, "Borrowing", True)

# User(UserID, Username, Email, Password, UserType)
def createNewUser(cursor):
    print("NEW USER CREATION")    
    while(True):
        username = ui.getUsername()
        if(username == "-1"):
            return
        usernames = getUsernames(cursor)
        if(username in usernames):
            print("Username already taken")
        else:
            break
    password = ui.getPassword()
    if(password == "-1"): return 
    email = ui.getEmail()
    if(email == "-1"): return
    member = "member"
    cursor.execute(
        f"""INSERT INTO User (Username, Email, Password, UserType) 
            VALUES ('{username}', '{email}', '{password}', '{member}')"""
    )
    



def getUserID(cursor, username):
    query = "SELECT UserID FROM User WHERE Username = ?"
    cursor.execute(query, (username,))
    result = cursor.fetchall()
    return result[0][0]

        
# Borrowing(BorrowingID, UserID FK, ItemID FK, BorrowDate, DueDate, Returned)
def insertIntoBorrowing(cursor, username, itemID):
    userID = getUserID(cursor, username)
   
    current_date_time = datetime.now()
    formatted_date = current_date_time.strftime("%Y-%m-%d")
    seven_days_later = current_date_time + timedelta(days=7)
    formatted_date_later = seven_days_later.strftime("%Y-%m-%d")

    if(validInsertion(cursor, userID, itemID)):
        cursor.execute(
        f"""INSERT INTO Borrowing (UserID,ItemID,BorrowDate,DueDate,Returned) VALUES ({userID},{itemID},{formatted_date},{formatted_date_later},{0})""")
    else:
        print(f"{username} is already borrowing such item")
    
def validInsertion(cursor, userID, itemID):
    querey = "SELECT UserID, ItemID FROM Borrowing WHERE UserID = ? AND ItemID = ?"
    cursor.execute(querey, (userID, itemID))
    result = cursor.fetchall()
    if(result):
        return False
    return True

def validatePassword(cursor, username, password):
    column_to_check = "Username"
    column_to_check_two = "Password"
    table_to_check = "User"

    query = f"SELECT * FROM {table_to_check} WHERE {column_to_check} = ? AND {column_to_check_two} = ?"
    cursor.execute(query, (username,password))
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False

def getUsernames(cursor):
    rows = getData(cursor, "User", False)
    usernames = []
    for row in rows:
        usernames.append(row[1])
    
    return usernames


    # INSERT NEW TUPLE INTO BORROWING
    

def displayData(cursor):
    getData(cursor, "User", True)
    getData(cursor, "Borrowing", True)
    getData(cursor, "Item", True)




# def returnBorrowedItem(cursor):

    

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
