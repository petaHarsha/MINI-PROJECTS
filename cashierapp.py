class cahierapp:
    def __init__(s):
        s.cart = []
        s.next_id = 1
        s.discounts = []
    def add_item(s, name, price,qty):
        item=item(s.next_id,name,price,qty)
        s.cart.append(item)
        s.next_id += 1
        print(f"Added {qty} x {name}(s) to cart.")
    def view_cart(s):
        if not s.cart:
            print("Your cart is empty.")
            return
        print("----- Your Cart -----")
        total = 0
        for item in s.cart:
            item_total = item.price * item.qty
            print(f"ID: {item.id}, Name: {item.name}, Price: ${item.price}, Quantity: {item.qty}, Total: ${item_total}")
            total += item_total
        print(f"Total Amount: ${total}")
    def remove_item(s, item_id):
        for item in s.cart:
            if item.id == item_id:
                s.cart.remove(item)
                print(f"Removed {item.name} from cart.")
                return
        print("Item not found in cart.")
    def apply_discount(s, code, percentage):
        s.discounts.append((code, percentage))
        print(f"Applied discount code '{code}' for {percentage}% off.")
    def calculate_total(s, code=None):
        total = sum(item.price * item.qty for item in s.cart)
        if code:
            for disc_code, percentage in s.discounts:
                if disc_code == code:
                    discount_amount = total * (percentage / 100)
                    total -= discount_amount
                    print(f"Discount of {percentage}% applied. You saved ${discount_amount}.")
                    break
            else:
                print("Invalid discount code.")
        print(f"Total Amount after discounts: ${total}")
        return total
class item:
    def __init__(s, id, name, price,qty):
        s.id = id
        s.name = name
        s.price = price
        s.qty=qty
def main():
    app = cahierapp()
    while True:
        print("\n----- Cashier App -----")
        print("1. Add Item to Cart")
        print("2. View Cart")
        print("3. Remove Item from Cart")
        print("4. Apply Discount Code")
        print("5. Calculate Total")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            qty = int(input("Enter item quantity: "))
            app.add_item(name, price,qty)
        elif choice == 2:
            app.view_cart()
        elif choice == 3:
            item_id = int(input("Enter item ID to remove: "))
            app.remove_item(item_id)
        elif choice == 4:
            code = input("Enter discount code: ")
            percentage = float(input("Enter discount percentage: "))
            app.apply_discount(code, percentage)
        elif choice == 5:
            code = input("Enter discount code (or press Enter to skip): ")
            code = code if code else None
            app.calculate_total(code)
        elif choice == 6:
            print("Exiting the Cashier App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")