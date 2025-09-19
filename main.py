print("=== Welcome to the PreWork Chatbot ===")

name = input("What is your name? ")
age = input("How old are you? ")

print("Nice to meet you, " + name + "! You are " + age + " years old.")

running = True
while running:
    print("\n--- Menu ---")
    print("1) Option 1 (placeholder)")
    print("2) Option 2 (placeholder)")
    print("3) Option 3 (placeholder)")
    print("4) Exit")

    choice = input(f"\nSo " + name + ", what do you need help with today? Pick 1-4: ")

    if choice == "4":
        print("Goodbye! Thank you for chatting with me.")
        break
    elif choice in ["1", "2", "3"]:
        print(f"Placeholder response for option {choice}")
    else:
        print("Please choose a valid option.")

