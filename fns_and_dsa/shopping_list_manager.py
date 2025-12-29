def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []

    def add_item():
        item = input("Enter the item to add: ")
        shopping_list.append(item)

    def remove_item():
        item = input("Enter item name to remove: ")
        if item not in shopping_list:
            print(f"{item} not in list")

        else:
            shopping_list.remove(item)

    def view_list():
            for item in shopping_list:
                print(item)

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item()

        elif choice == '2':
            remove_item()

        elif choice == '3':
            view_list()

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
