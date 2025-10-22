class cryptopaymentapp:
    def __init__(s):
        s.wallets = {}
    def create_wallet(s, user):
        if user in s.wallets:
            print(f"Wallet for {user} already exists.")
        else:
            s.wallets[user] = 0.0
            print(f"Wallet created for {user}.")
    def add_funds(s, user, amount):
        if user in s.wallets:
            s.wallets[user] += amount
            print(f"Added ${amount} to {user}'s wallet. New balance: ${s.wallets[user]}")
        else:
            print(f"Wallet for {user} does not exist.")
    def make_payment(s, sender, receiver, amount):
        if sender not in s.wallets:
            print(f"Sender wallet for {sender} does not exist.")
            return
        if receiver not in s.wallets:
            print(f"Receiver wallet for {receiver} does not exist.")
            return
        if s.wallets[sender] >= amount:
            s.wallets[sender] -= amount
            s.wallets[receiver] += amount
            print(f"Payment of ${amount} from {sender} to {receiver} successful.")
            print(f"{sender}'s new balance: ${s.wallets[sender]}")
            print(f"{receiver}'s new balance: ${s.wallets[receiver]}")
        else:
            print(f"Insufficient funds in {sender}'s wallet.")
    def view_balance(s, user):
        if user in s.wallets:
            print(f"{user}'s wallet balance: ${s.wallets[user]}")
        else:
            print(f"Wallet for {user} does not exist.")
def main():
    app = cryptopaymentapp()
    while True:
        print("\n----- Crypto Payment App -----")
        print("1. Create Wallet")
        print("2. Add Funds")
        print("3. Make Payment")
        print("4. View Balance")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            user = input("Enter user name: ")
            app.create_wallet(user)
        elif choice == 2:
            user = input("Enter user name: ")
            amount = float(input("Enter amount to add: "))
            app.add_funds(user, amount)
        elif choice == 3:
            sender = input("Enter sender user name: ")
            receiver = input("Enter receiver user name: ")
            amount = float(input("Enter amount to pay: "))
            app.make_payment(sender, receiver, amount)
        elif choice == 4:
            user = input("Enter user name: ")
            app.view_balance(user)
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")