class Coffee:
    def __init__(s,name,price):
        s.name,s.price=name,price
class CoffeeMachine:
    def __init__(s):
        s.menu=[
            Coffee("Espresso",3),
            Coffee("Latte",4),
            Coffee("Cappuccino",4.5),
            Coffee("Americano",2.5)
        ]
        s.balance=0
    def show_menu(s):
        print("----- Coffee Menu -----")
        for i,c in enumerate(s.menu,1):
            print(f"{i}. {c.name} - ${c.price}")
        print("-----------------------")
    def insert_money(s,amount):
        s.balance+=amount
        print(f"Inserted ${amount}. Current balance: ${s.balance}")
    def buy_coffee(s,choice):
        if 1<=choice<=len(s.menu):
            coffee=s.menu[choice-1]
            if s.balance>=coffee.price:
                s.balance-=coffee.price
                print(f"Dispensing {coffee.name}. Enjoy!")
                print(f"Remaining balance: ${s.balance}")
            else:
                print("Insufficient balance. Please insert more money.")
        else:
            print("Invalid choice. Please select a valid coffee.")
    def refund(s):
        print(f"Refunding ${s.balance}.")
        s.balance=0
def main():
    m=CoffeeMachine()
    while True:
        m.show_menu()
        print("1. Insert Money")
        print("2. Buy Coffee")
        print("3. Refund")
        print("4. Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            m.show_menu()
        elif choice==2:
            m.insert_money(float(input("Enter amount to insert: ")))
        elif choice==3:
            m.show_menu()
            m.buy_coffee(int(input("Enter coffee choice number: ")))
        elif choice==4:
            m.refund()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__=="__main__":
    main()