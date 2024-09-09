class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        self.contacts[name] = {"phone": phone, "email": email}
        print(f"Contact '{name}' added!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts yet!")
        else:
            print("Your contacts:")
            for name, details in self.contacts.items():
                print(f"{name}: {details['phone']}, {details['email']}")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"{name}: {self.contacts[name]['phone']}, {self.contacts[name]['email']}")
        else:
            print(f"Contact '{name}' not found!")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted!")
        else:
            print(f"Contact '{name}' not found!")
def main():
    contact_book = ContactBook()
    while True:
        print("\n1. Add contact")
        print("2. View contacts")
        print("3. Search contact")
        print("4. Delete contact")
        print("5. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contact_book.add_contact(name, phone, email)
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            name = input("Enter name to search: ")
            contact_book.search_contact(name)
        elif choice == "4":
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
