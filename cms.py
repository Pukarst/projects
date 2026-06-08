contacts = {}
print('---WELCOME TO THE CONTACT MANAGEMENT SYSTEM---')
def add_contact():
    name = input("Enter the name: ")
    phone_number = int(input("Enter the phone number: "))
    contacts[name] = phone_number
    print("Contact added!")

def view_contacts():
    if contacts:
        print("\nContacts List:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts found.")

def search_contact():
    name = input("Enter the name to search: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"Contact {name} not found.")

def contact_book():
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")
        
        choice = input("Choose the valid option: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please choose the given options.")
contact_book()
