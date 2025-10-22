class CourierApp:
    def __init__(s):
        s.orders=[]
    def add_order(s,name,address,charge,status="Pending"):
        s.orders.append({"name":name,"address":address,"charge":charge,"status":status})
    def view_orders(s):
        if not s.orders:
            print("No orders available.")
            return
        for i ,o in enumerate(s.orders,1):
            print(f"{i}. Name: {o['name']}, Address: {o['address']}, Charge: ${o['charge']}, Status: {o['status']}")
    def update_status(s,i):
        if 0<i<=len(s.orders):
            s.orders[i-1]['status']="Delivered"
            print(f"Order {i} status updated to Delivered.")
        else:
            print("Invalid order number.")
    def remove_order(s,i):
        if 0<i<=len(s.orders):
            s.orders.pop(i-1)
            print(f"Order {i} removed.")
        else:
            print("Invalid order number.")
    def total_revenue(s):
        total=sum(o['charge'] for o in s.orders if o['status']=="Delivered")
        print(f"Total Revenue from Delivered Orders: ${total}")
    def run(s):
        while True:
            print("1. Add Order")
            print("2. View Orders")
            print("3. Update Order Status")
            print("4. Remove Order")
            print("5. Total Revenue")
            print("6. Exit")
            choice=int(input("Enter your choice: "))
            if choice==1:
                name=input("Enter customer name: ")
                address=input("Enter delivery address: ")
                charge=float(input("Enter delivery charge: "))
                s.add_order(name,address,charge)
            elif choice==2:
                s.view_orders()
            elif choice==3:
                s.view_orders()
                i=int(input("Enter order number to update status: "))
                s.update_status(i)
            elif choice==4:
                s.view_orders()
                i=int(input("Enter order number to remove: "))
                s.remove_order(i)
            elif choice==5:
                s.total_revenue()
            elif choice==6:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
CourierApp().run()
