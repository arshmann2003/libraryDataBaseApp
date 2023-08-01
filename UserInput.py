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
    
    def getTitle():
        return input("Enter the Items title: ").strip()
        
        