from contacts import Contacts
from menu import MainMenu


if __name__ == '__main__':
    while True:
        # Show main menu    
        option = MainMenu.showMainMenu()
        # Create an instance of the Contacts class
        contacts = Contacts()
        match(option):
            case 1: # Add contact
                # Show add contact menu
                MainMenu.showMenuAddContact()
                # Get contact data
                name, email, phone = MainMenu.addContact()
                # Add contact to the list
                contacts.add(name, email, phone)

            case 2: # Contact list
                MainMenu.showMenuShowContacts()
                contacts.show_all_contacts()

            case 3: # Search contact
                MainMenu.showMenuSearchContact()
                email = MainMenu.searchContact()
                contact = contacts.search(email)
                if contact:
                    print(contact)
                else:
                    print('Contact not found')

            case 4: # Update contact
                MainMenu.showMenuUpdate()
                MainMenu.showMenuShowContacts()
                contacts.show_all_contacts()
                email = MainMenu.searchContact()
                contact = contacts.search(email)
                if contact:
                    name, phone = MainMenu.getContactData()
                    response = contacts.update(name, phone, contact['email'])
                    print('contact updated') 
                else:
                    print('Contact not found')
            case 5: # Exit
                print('Goodbye!')
                break