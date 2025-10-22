class CarService:
    def __init__(s):
        s.services = {
            1:("Basic Wash",30),
            2:("Deluxe Wash",50),
            3:("Premium Wash",80),
            4:("oil Change",60),
            5:("Tire Rotation",40),
            6:("Interior Cleaning",70),
            7:("Full Service",120),
            8:("Engine Detailing",150),
            9:("Paint Protection",200)
        }
        s.cart = []
    def show_services(s):
        print("----- Car Wash Services Menu -----")
        for key, (name, price) in s.services.items():
            print(f"{key}. {name} - ${price}")
        print("----------------------------------")
    def add_to_cart(s,choice):
        if choice in s.services:
            s.cart.append(s.services[choice])
            print(f"Added {s.services[choice][0]} to cart.")
        else:
            print("Invalid service choice.")
    def view_cart(s):
        if not s.cart:
            print("Your cart is empty.")
            return
        print("----- Your Cart -----")
        total = 0
        for i, (name, price) in enumerate(s.cart,1):
            print(f"{i}. {name} - ${price}")
            total += price
        print(f"Total: ${total}")
    def checkout(s):
        if not s.cart:
            print("Your cart is empty. Add services before checkout.")
            return
        s.view_cart()
        confirm = input("Do you want to proceed to checkout? (yes/no): ").strip().lower()
        if confirm == 'yes':
            print("Checkout successful. Thank you for using our car wash services!")
            s.cart.clear()
        else:
            print("Checkout cancelled.")
def main(): 
    app = CarService()
    while True:
        app.show_services()
        print("1. Add Service to Cart")
        print("2. View Cart")
        print("3. Checkout")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            service_choice = int(input("Enter the service number to add to cart: "))
            app.add_to_cart(service_choice)
        elif choice == 2:
            app.view_cart()
        elif choice == 3:
            app.checkout()
        elif choice == 4:
            print("Exiting the Car Wash Services App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")






