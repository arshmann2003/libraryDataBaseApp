class UserInput:
    attributes = {"Item": "id, ItemType, Title, AUthor, Publisher, Availability",
                  "User": "UserID, Username, Email, Password, UserType",
                  "Borrowing" : "BorrowingID, UserID, ItemID, BorrowDate, DueDate, Returned",
                  "Donation": "DonationID, UserID, ItemID, DonationDate",
                  "Event": "EventID, EventType, Title, Description, Date, Location, Audience",
                  "Attendee": "EventID, UserID"
                  }
# Event(EventID, EventType, Title, Description, Date, Location, Audience)

    def getAuthorName():
        return input("Enter the author's name: ").strip()
        
    def printData(list, table):
        print("------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"Table:{table}")
        print(UserInput.attributes[table])
        for row in list:
            list = ""
            print("------------------------------------------------------------------------------------------------------------------------------------------------------")
            for col in row:
                list += str(col)
                list += " | "
            print(list)
        print("------------------------------------------------------------------------------------------------------------------------------------------------------")
    
    def getTitle():
        return input("Enter the Items title: ").strip()
    
    def getItemID(rows, opt):
        validIDs = []
        for row in rows:
            validIDs.append(int(row[0]))
    
        while(True) :
            if(opt==2):
                itemID = input("Enter id of Item you would like to borrow | D to display items | Q to quit: ").strip()
            elif(opt==3):
                itemID = input("Enter id of the item you want to return: ").strip()
            elif(opt==6):
                itemID = input("Enter id of the Event you want to join: ")
            if(itemID.isdigit() and (int(itemID) in validIDs)):
                return itemID
            elif(itemID.upper()=="D" and opt == 2):
                UserInput.printData(rows, "Item")
            elif(itemID.upper()=="Q" and opt==2):
                return -1
            elif(opt==2):
                print(f"Invalid ids must range {validIDs[0]}-{validIDs[len(validIDs)-1]} ")
            else:
                x = ""
                for id in validIDs:
                    x += str(id)
                    if(id != validIDs[len(validIDs)-1]):
                        x += ","
                print(f"Invalid id range[{x}]")

    def getUsername():
        return input("Enter your username (-1 to quit): ")

    def getPassword():
        return input("Enter your password (-1 to quit): ")

    def getEmail():
        return input("Enter email: ")
    
    def returningUser():
        ans = input("Do you have an account Y or N: ")
        if(ans == "Y"):
            return True
        return False
    
    def getStatus():
        userType = input("Choose one [M: Member, L: Librarian, V: Volunteer]").strip()
        if(userType == "M"):
            return "Member"
        elif(userType == "L"):
            return "Librarian"
        else:
            return "Volunteer"
    def getItemTitle():
        return input ("Enter the title of your item: ")
    
    def userNotFound(i):
        print("--------------------------------------------------------")
        if(i!=0):
            print("Username not found")
        print("0: exit")
        print("1: display names of users borrowing items")
        print("2: Enter Username")
        choice = input("Enter Choice: ")
        print("--------------------------------------------------------")
        return choice

    def displayUsernames(list):
        for item in list:
            print(item)
        print("--------------------------------------------------------")

    def accountExists():
        choice = ""
        while choice not in ["Y", "N"]:
            choice = input("Do you have an existing account Y or N: ")
        
        if(choice == "Y"):
            return True
        return False
    
    def titleName():
        return input("title of item: ")

    def authorName():
        return (input("Author name: "))
    
    def itemType():
        return input("Item Type: ")
    
    def publisher():
        return input("Publisher: ")
    
    def getDataOption():
        print("-----------------------")
        print("1: Item table")
        print("2: Borrowing table")
        print("3: Users table")
        print ("4: Donation table")
        print("5: Event table")
        print("6: Attendee table")
        choice = input("Which table: ")
        print("-----------------------")
        return choice

    def getEventType():
        validTypes = ["Book Club","Art Show","Film Screening"]
        userInput = ""
        while(userInput not in validTypes):
            userInput = input("Event Type (press 1 for event types): ")
            if(userInput == "1"):
                print(":::::::::::::::::::::::")
                for type in validTypes:
                    print(type)
                print(":::::::::::::::::::::::")
        return userInput
    
    def eventError():
        print("User is already in this event")