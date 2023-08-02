class UserInput:
    attributes = {"Item": "id, ItemType, Title, AUthor, Publisher, Availability",
                  "User": "UserID, Username, Email, Password, UserType",
                  "Borrowing" : "BorrowingID, UserID, ItemID, BorrowDate, DueDate, Returned"
                  }

    def getAuthorName():
        return input("Enter the author's name: ").strip()
        
    def printData(list, table):
        print("---------------------------------------------------------------------------")
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
        
        print(validIDs)
            
        while(True) :
            itemID = input("Enter id of Item you would like to borrow or D to display items or Q to quit: ").strip()
            if(itemID.isdigit() and (int(itemID) in validIDs)):
                return int(itemID)
            elif(itemID=="D"):
                return -1
            elif(itemID=="Q"):
                return -2
            else:
                print(f"Invalid ids must range {validIDs[0]}-{validIDs[len(validIDs)-1]} ")

        