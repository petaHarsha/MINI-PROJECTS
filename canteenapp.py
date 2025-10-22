class CanteenApp:
    def __init__(s):
        s.menu = {
            "Burger": 5.0,
            "Pizza": 8.0,
            "Sandwich": 4.0,
            "Pasta": 7.0,
            "Salad": 3.5
        }
        s.balance = 0.0

    def show_menu(s):
        print("----- Canteen Menu -----")
        for item, price in s.menu.items():
            print(f"{item} - ${price}")
        print("------------------------")

    def add_funds(s, amount):
        s.balance += amount
        print(f"Added ${amount}. Current balance: ${s.balance}")

    def order_item(s, item):
        if item in s.menu:
            price = s.menu[item]
            if s.balance >= price:
                print(f"Ordering {item} for ${price}. Press Enter to confirm...")
                input()
                quantity = int(input(f"Enter quantity of {item}: "))
                total_cost = price * quantity
                if s.balance >= total_cost:
                    s.balance -= total_cost
                    print(f"Ordered {quantity} x {item}(s) for ${total_cost}. Remaining balance: ${s.balance}")
                else:
                    print("Not enough balance for that quantity.")
            else:
                print("Insufficient balance. Please add more funds.")
        else:
            print("Item not available in the menu.")

    def view_balance(s):
        print(f"Current balance: ${s.balance}")

    def add_item(s, item, price):
        print(f"Adding {item} to menu at price ${price}. Press Enter to confirm...")
        input()
        s.menu[item] = price
        print(f"Added {item} to menu at price ${price}.")

    def run(s):
        while True:
            print("\n----- Canteen App -----")
            print("1. Show Menu")
            print("2. Add Funds")
            print("3. Order Item")
            print("4. View Balance")
            print("5. Add Item to Menu")
            print("6. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                s.show_menu()
            elif choice == 2:
                amount = float(input("Enter amount to add: "))
                s.add_funds(amount)
            elif choice == 3:
                item = input("Enter item name to order: ")
                s.order_item(item)
            elif choice == 4:
                s.view_balance()
            elif choice == 5:
                item = input("Enter item name to add: ")
                price = float(input("Enter item price: "))
                s.add_item(item, price)
            elif choice == 6:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
