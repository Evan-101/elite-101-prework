def display_menu():
    print("=== Lunch Menu ===")
    print("1. Salad")
    print("2. Sandwich")
    print("3. Pizza")
    print("4. Exit")
    print("===================")

def greet_user():
    name = input("What's your name? ")
    age = input("How old are you? ")
    print(f"\nHello {name}! You are {age} years old. Welcome to the lunch menu!")

def main():
    greet_user()

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print("You have selected Salad your oder will be ready soon.")
        elif choice == '2':
            print("You have selected Sandwich your order will be ready soon.")
        elif choice == '3':
            print("You have selected Pizza your order will be ready soon.")
        elif choice == '4':
            print("Exiting the lunch menu. Enjoy your day!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()