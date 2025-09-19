
"""
    Welcome to Elite 101 this program is a starter for your chatbot project.
    The starter prompts the user to enter their name and then greets them with a personalized message.

    Functions:
        get_user_name(): Prompts the user to enter their name and returns it.
        greet_user(name): Prints a greeting message using the provided name.
        main(): Main function that orchestrates the user input and greeting process.

    Execution:
        When the script is run directly (not imported as a module), it will execute the main() function.
"""

def get_user_name():
    return input("Please enter your name: ")

def greet_user(name):
    print(f"Hello, {name}! I am the Chatbot. How may I help you?\n")

def main():
    # Start chatbot
    user_name = get_user_name()
    greet_user(user_name)

    # Menu loop
    while True:
        print("Please choose from the following options:")
        print("1. Placeholder Option 1")
        print("2. Placeholder Option 2")
        print("3. Placeholder Option 3")
        print("4. Exit the conversation")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            print("You chose Option 1 — [placeholder].\n")
        elif choice == "2":
            print("You chose Option 2 — [placeholder].\n")
        elif choice == "3":
            print("You chose Option 3 — [placeholder].\n")
        elif choice == "4":
            print("Goodbye! Thanks for chatting.")
            break
        else:
            print("Please choose 1, 2, 3, or 4.\n")

if __name__ == "__main__":
    main()
