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
    
    def getItemID(rows, opt):
        validIDs = []
        for row in rows:
            validIDs.append(int(row[0]))
    
        while(True) :
            if(opt==2):
                itemID = input("Enter id of Item you would like to borrow | D to display items | Q to quit: ").strip()
            elif(opt==3):
                itemID = input("Enter id of the item you want to return: ").strip()
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