import json
import os

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self.load_contacts()

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        for i, contact in enumerate(self.contacts):
            print(f"\nContact {i + 1}:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")

    def update_contact(self, index, contact):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = contact
            self.save_contacts()
        else:
            print("Invalid index")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            self.contacts.pop(index)
            self.save_contacts()
        else:
            print("Invalid index")

    def save_contacts(self):
        with open(self.filename, 'w') as f:
            json.dump(self.contacts, f)

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contact = {"name": name, "phone": phone, "email": email}
            contact_book.add_contact(contact)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            contact_book.view_contacts()
            index = int(input("Enter the contact number to update: ")) - 1
            name = input("Enter new name: ")
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            contact = {"name": name, "phone": phone, "email": email}
            contact_book.update_contact(index, contact)
        elif choice == '4':
            contact_book.view_contacts()
            index = int(input("Enter the contact number to delete: ")) - 1
            contact_book.delete_contact(index)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
