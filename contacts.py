class BaseClass:
    # LISTA DE TODOS LOS CONTACTOS
    contacts = []

    # guarda cada contacto en la lista
    def add_contact(self, name, email, phone):
        user_data = {'name': name, 'email': email, 'phone': phone}
        self.contacts.append(user_data)
    
    def update_contact(self, email. name, phone):
        contact = self.search_contact(email)
        if contact is not None:
            contact['name'] = name
            contact['phone'] = phone
            return True
        return False

    def search_contact(self):
        pass

    @classmethod
    def all_contacts(cls):
        return cls.contacts

class Contacts(BaseClass):
    def add(self, name, email, phone):
        self.add_contact(name, email, phone)
    
    def show_all_contacts(self):
        contacts = self.all_contacts()
        for contact in contacts:
            print(contact['name'], '\t', contact['email'], '\t', contact['phone'])
    
    def search(self):
        pass

    def update(self, email, name, phone):
        return self.update_contact(email, name, phone)


