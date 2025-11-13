print("=== Welcome to the Prework Chatbot ===")

name = input("What is your name? ")
age = input("How old are you? ")

print("Nice to meet you, " + name + "! You are " + age + " years old.")

running = True

while running:
    print("\n--- Menu ---")
    print("(1) Return or Exchange")
    print("(2) Track an Order")
    print("(3) Exit")

    choice = input(f"\nSo {name}, what do you need help with today? Pick 1-3: ")

    if choice == "3":
        print("Goodbye! Thank you for chatting with me.")
        break

    elif choice == "1":
        print("\n--- Return or Exchange ---")
        order_num = input("Please enter your order number: ")
        days = input("How many days ago was the item delivered? ")

        # check eligibility
        if days.isdigit() and int(days) <= 30:
            print("Your return/exchange request has been submitted.")
            print("You’ll receive an email with further instructions soon.")
        else:
            print("Sorry, this order is no longer eligible for return or exchange.")

    elif choice == "2":
        print("\n--- Track an Order ---")
        order_num = input("Please enter your order number (e.g., A123 or B456): ")

        # simple fake order data
        orders = {
            "A123": "Delivered",
            "B456": "Shipped",
            "C789": "Processing"
        }

        if order_num in orders:
            print("Order", order_num, "status:", orders[order_num])
        else:
            print("Sorry, that order number was not found.")

    else:
        print("Please choose a valid option (1-3).")
