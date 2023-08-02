class UserInput:
    attributes = {"Item": "id, ItemType, Title, AUthor, Publisher, Availability",
                  "User": "UserID, Username, Email, Password, UserType",
                  "Borrowing" : "BorrowingID, UserID, ItemID, BorrowDate, DueDate, Returned"
                  }

    def getAuthorName():
        return input("Enter the author's name: ").strip()
        
    def printData(list, table):
        print("---------------------------------------------------------------------------")
        print(f"Table:{table}")
        print(UserInput.attributes[table])
        for row in list:
            list = ""
            print("---------------------------------------------------------------------------")
            for col in row:
                list += str(col)
                list += " | "
            print(list)
        print("---------------------------------------------------------------------------")
    
    def getTitle():
        return input("Enter the Items title: ").strip()
    
    def getItemID(rows):
        validIDs = []
        for row in rows:
            validIDs.append(int(row[0]))
    
        while(True) :
            itemID = input("Enter id of Item you would like to borrow | D to display items | Q to quit: ").strip()
            if(itemID.isdigit() and (int(itemID) in validIDs)):
                return itemID
            elif(itemID.upper()=="D"):
                UserInput.printData(rows, "Item")
            elif(itemID.upper()=="Q"):
                return -1
            else:
                print(f"Invalid ids must range {validIDs[0]}-{validIDs[len(validIDs)-1]} ")

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