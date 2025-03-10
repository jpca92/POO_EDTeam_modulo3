class MainMenu:
    
    def showMainMenu():
        print("1. Add contact")
        print("2. Show contacts")
        print("3. Search contact")
        print("4. Edit contact")
        print("5. Exit")
        option = int(input("Select an option: "))
        while option > 5 or option < 1:
            print("Invalid option")
            option = int(input("Select an option: "))
        else:
            return option
    @staticmethod
    def showMenuAddContact():
        print('ADD CONTACT')
    
    @staticmethod
    def addContact():
        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        return name, email, phone
    
    @staticmethod
    def showMenuShowContacts():
        print('SHOW CONTACTS')
        print('Name\t\tEmail\t\tPhone')
    
    @staticmethod
    def showMenuSearchContact():
        print('SEARCH CONTACT')
        
    
    @staticmethod
    def searchContact():
        email = input('Enter the email: ')
        return email
    
    @staticmethod
    def showMenuUpdate():
        print('EDIT CONTACT')
    
    @staticmethod
    def getContactEmail():
        email = input('Enter the email: ')
        return email
    
    def getContactData():
        name = input('Enter the name: ')
        phone = input('Enter the phone: ')
        return name, phone