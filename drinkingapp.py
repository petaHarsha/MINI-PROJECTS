class Drink:
    def __init__(s,name,prive,stock):
        s.name,s.price,s.stock=name,prive,stock


class DrinkingApp:
    def __init__(s):
        s.drinks,s.cart=[],[]
    def add_drink(s,name,price,stock):
        s.drinks.append(Drink(name,price,stock))
    def view_drinks(s):
        if not s.drinks:
            print("No drinks available.")
            return
        for d in s.drinks:
            print(f"Name: {d.name} | Price: ${d.price} | Stock: {d.stock}")
    def order_drink(s,name,qty):
        for d in s.drinks:
            if d.name==name:
                if d.stock>=qty:
                    d.stock-=qty
                    s.cart.append((d.name,d.price,qty))
                    print(f"Added {qty} x {d.name} to cart.")
                else:
                    print(f"Insufficient stock for {d.name}.")
                return
        print(f"{name} not found.")

    def update_drink(s,name,price=None,stock=None):
        for d in s.drinks:
            if d.name==name:
                if price :
                    d.price=price
                if stock is not None:
                    d.stock=stock
                print(f"Updated {name}.")
                return
            print(f"{name} this drnk is not found")
    def bill(s):
        total=sum(price*qty for _,price,qty in s.cart)
        print("----- Bill -----")
        if not s.cart:
            print("No items in cart.")
            return
        for name,price,qty in s.cart:
            print(f"{qty} x {name} @ ${price} each")
        print(f"Total Amount: ${total}")
        print("----------------")
    def main():
        app=DrinkingApp()
        while True:
            print("1. Add Drink")
            print("2. View Drinks")
            print("3. Order Drink")
            print("4. Update Drink")
            print("5. Generate Bill")
            print("6. Exit")
            choice=int(input("Enter your choice: "))
            if choice==1:
                name=input("Enter drink name: ")
                price=float(input("Enter drink price: "))
                stock=int(input("Enter drink stock: "))
                app.add_drink(name,price,stock)
            elif choice==2:
                app.view_drinks()
            elif choice==3:
                name=input("Enter drink name to order: ")
                qty=int(input("Enter quantity: "))
                app.order_drink(name,qty)
            elif choice==4:
                name=input("Enter drink name to update: ")
                price=input("Enter new price (or press Enter to skip): ")
                stock=input("Enter new stock (or press Enter to skip): ")
                price=float(price) if price else None
                stock=int(stock) if stock else None
                app.update_drink(name,price,stock)
            elif choice==5:
                app.bill()
            elif choice==6:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
