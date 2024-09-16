import json
import os

CONTACT_FILE = 'contacts.json'

def load_contacts():
    """Load contacts from a JSON file."""
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    """Save contacts to a JSON file."""
    with open(CONTACT_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    """Add a new contact to the contact book."""
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    
    if name in contacts:
        print("Contact already exists!")
    else:
        contacts[name] = {'phone': phone, 'email': email}
        print("Contact added.")

def view_contacts(contacts):
    """View all contacts in the contact book."""
    if not contacts:
        print("No contacts available.")
    else:
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print("-" * 20)

def update_contact(contacts):
    """Update an existing contact."""
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        contacts[name] = {'phone': phone, 'email': email}
        print("Contact updated.")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    """Delete a contact from the contact book."""
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

def main():
    """Main function to run the contact book application."""
    contacts = load_contacts()
    
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
