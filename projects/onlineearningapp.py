class OnlineEarningapp:
    def __init__(s):
        s.balance=0
    def add_earning(s,amount):
        s.balance+=amount
        print(f"Added earning: ${amount}. Current balance: ${s.balance}")
    def view_balance(s):
        print(f"Current balance: ${s.balance}")
    def withdraw(s,amount):
        if amount<=s.balance:
            s.balance-=amount
            print(f"Withdrew: ${amount}. Remaining balance: ${s.balance}")
        else:
            print("Insufficient balance for withdrawal.")
    def do_task(s):
        s.balance+=10
        print("\n")
        print("task completed. Earned $10.")

    def referral(s):
        s.balance+=15
        print("\n")
        print("Referral successful. Earned $15.")
    def menu(s):
        while True:
            print("\n")
            print("----- Online Earning App -----")
            print("1. Add Earning")
            print("2. View Balance")
            print("3. Withdraw")
            print("4. Do Task")
            print("5. Referral")
            print("6. Exit")
            choice=int(input("Enter your choice: "))
            if choice==1:
                amount=float(input("Enter amount to add: "))
                s.add_earning(amount)
            elif choice==2:
                s.view_balance()
            elif choice==3:
                amount=float(input("Enter amount to withdraw: "))
                s.withdraw(amount)
            elif choice==4:
                s.do_task()
            elif choice==5:
                s.referral()
            elif choice==6:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")