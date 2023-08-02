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
    itemID = ui.getItemID(rows, 2)
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
        createNewUser(cursor)

# User(UserID, Username, Email, Password, UserType)
def createNewUser(cursor):
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
    return username
    

def getUserID(cursor, username):
    query = "SELECT UserID FROM User WHERE Username = ?"
    cursor.execute(query, (username,))
    result = cursor.fetchall()
    if(result):
        return result[0][0]
    return False

        
# Borrowing(BorrowingID, UserID FK, ItemID FK, BorrowDate, DueDate, Returned)
def insertIntoBorrowing(cursor, username, itemID):
    userID = getUserID(cursor, username)
   
    current_date_time = datetime.now()
    formatted_date = current_date_time.strftime("%Y-%m-%d")
    seven_days_later = current_date_time + timedelta(days=7)
    formatted_date_later = seven_days_later.strftime("%Y-%m-%d")

    if(validBorrowingInsertion(cursor, userID, itemID)):
        cursor.execute(
        f"""INSERT INTO Borrowing (UserID,ItemID,BorrowDate,DueDate,Returned) VALUES ({userID},{itemID},{formatted_date},{formatted_date_later},{0})""")
    else:
        print(f"{username} is already borrowing such item")
    
def validBorrowingInsertion(cursor, userID, itemID):
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

def displayData(cursor):
    x = ui.getDataOption()
    if(x == '1'):
        getData(cursor, "Item", True)
    elif(x == '2'):
        getData(cursor, "Borrowing", True)
    elif(x == '3'):
        getData(cursor, "User", True)
    elif(x == '4'):    
        getData(cursor, "Donation", True)
    elif(x == '5'):
        getData(cursor, "Event", True)
    elif(x == '6'):
        getData(cursor, "Attendee", True)



def displayUsersBorrowing(cursor):
    querey = "SELECT UserID FROM Borrowing"
    cursor.execute(querey)
    result = cursor.fetchall()
    usersBorrowing = []
    for id in result:
        usersBorrowing.append((int(id[0])))
    usersBorrowing = list(set(usersBorrowing))
    querey = "SELECT Username FROM User WHERE UserID = ?"
    usernames = []
    for i in usersBorrowing:
        cursor.execute(querey, (i,))
        result = cursor.fetchall()
        usernames.append(result[0][0])
    ui.displayUsernames(usernames)
    

def returnBorrowedItem(cursor):
    username = ""
    if(username == "-1"):
        return
    i = 0
    while(True):
        userID = getUserID(cursor, username)
        if(userID != False):
            break
        else:
            choice = ui.userNotFound(i)      
            if(choice=="0"):
                return
            elif(choice=="1"):
                displayUsersBorrowing(cursor)
            username = ui.getUsername()
        i+=1
    querey = "SELECT ItemID FROM Borrowing WHERE UserID = ?"
    cursor.execute(querey, (userID,))
    result = cursor.fetchall()
    querey2 = "SELECT * FROM Item WHERE ItemID = ?"
    usersItems = []
    for row in result:
        cursor.execute(querey2, (row[0],))
        result = cursor.fetchall()
        x = []
        for item in result:
            for sub in item:
                x.append(sub)
        usersItems.append(x)
    ui.printData(usersItems, "Item")
    itemID = ui.getItemID(usersItems, 3)
    
    deleteQuerey = "DELETE FROM Borrowing WHERE UserId = ? AND ItemID = ?"
    cursor.execute(deleteQuerey, (userID, itemID))


# Insert into Item
def donateItem(cursor):
    usernames = getUsernames(cursor)
    username = ""
    while(True):
        if(not ui.accountExists()):
            username = createNewUser(cursor)
            break
        else:
            username = ui.getUsername()
            if(username in usernames):
                break
            else:
                print("Username not found")
            if(username == "-1"):
                return
    userID = getUserID(cursor, username)
    title = ui.titleName()
    author = ui.authorName()
    publisher = ui.publisher()
    itemType = ui.itemType()
    current_date_time = datetime.now()
    formatted_date = current_date_time.strftime("%Y-%m-%d")
    cursor.execute(
        f"""INSERT INTO Item (ItemType, Title, Author, Publisher, Availability) VALUES ('{itemType}','{title}','{author}','{publisher}',{1})"""
    )
    inserted_item_id = cursor.lastrowid
    cursor.execute(
        f"""INSERT INTO Donation (UserID, ItemID, DonationDate) VALUES ({userID},{inserted_item_id},'{formatted_date}')"""
    )

def findEvent(cursor):
    eventType = ui.getEventType()
    querey = f"SELECT * FROM Event WHERE EventType = ?"
    cursor.execute(querey, (eventType,))
    result = cursor.fetchall()
    ui.printData(result, "Event")
    return result

def registerEvent(cursor):
    usernames = getUsernames(cursor)
    username = ""
    while(True):
        if(not ui.accountExists()):
            username = createNewUser(cursor)
            break
        else:
            username = ui.getUsername()
            if(username in usernames):
                break
            else:
                print("Username not found")
            if(username == "-1"):
                return
    userID = getUserID(cursor, username)
    events = findEvent(cursor)
    eventID = ui.getItemID(events, 6)
    querey = "SELECT * FROM Attendee WHERE EventID = ? AND UserID = ?"
    cursor.execute(querey, (eventID, userID))
    result = cursor.fetchall()
    if(not result):
        cursor.execute(
            f"""INSERT INTO Attendee (EventID, UserID) VALUES ({eventID},{userID})"""
        )
    else:
        ui.eventError()

def volunteerForLibrary(cursor):
    usernames = getUsernames(cursor)
    username = ""
    while(True):
        if(not ui.accountExists()):
            username = createNewUser(cursor)
            break
        else:
            username = ui.getUsername()
            if(username in usernames):
                break
            else:
                print("Username not found")
            if(username == "-1"):
                return
    userID = getUserID(cursor, username)
    querey = f"UPDATE User SET UserType = 'Volunteer' WHERE UserID = ?;"
    cursor.execute(querey, (userID,))
    
def askHelp(cursor):
    return ""
