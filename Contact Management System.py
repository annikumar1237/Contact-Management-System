import pickle

def save_data():
    with open("contacts.pkl", "wb") as file:
        pickle.dump(contacts, file)

def load_data():
    try:
        with open("contacts.pkl", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}

contacts = load_data()  # Existing data load karna
import pickle

contacts = load_data()

# Functions
def add_contact(name, phone, email):
    if name in contacts:
        print("Yeh contact already exist karta hai.")
    else:
        contacts[name] = (phone, email)
        print("Contact successfully add kar diya gaya.")

def view_contacts():
    if not contacts:
        print("Koi contacts nahi hain.")
    else:
        for name, details in sorted(contacts.items()):
            print(f"Name: {name}, Phone: {details[0]}, Email: {details[1]}")

def search_contact(name):
    if name in contacts:
        print(f"Contact mil gaya: {name}, Phone: {contacts[name][0]}, Email: {contacts[name][1]}")
    else:
        print("Contact nahi mila.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print("Contact delete kar diya gaya.")
    else:
        print("Contact nahi mila.")

def modify_contact(name, phone=None, email=None):
    if name in contacts:
        current_phone, current_email = contacts[name]
        new_phone = phone if phone else current_phone
        new_email = email if email else current_email
        contacts[name] = (new_phone, new_email)
        print("Contact update kar diya gaya.")
    else:
        print("Contact nahi mila.")

def save_data():
    with open("contacts.pkl", "wb") as file:
        pickle.dump(contacts, file)

def menu():
    while True:
        print("\n----- Contact Manager -----")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Modify Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)

        elif choice == '2':
            view_contacts()

        elif choice == '3':
            name = input("Enter name to search: ")
            search_contact(name)

        elif choice == '4':
            name = input("Enter name to delete: ")
            delete_contact(name)

        elif choice == '5':
            name = input("Enter name to modify: ")
            phone = input("Enter new phone (leave blank to skip): ")
            email = input("Enter new email (leave blank to skip): ")
            modify_contact(name, phone, email)

        elif choice == '6':
            print("Program ko exit kiya ja raha hai.")
            save_data()
            break
        else:
            print("Invalid choice, please try again.")

# Run the program
menu()