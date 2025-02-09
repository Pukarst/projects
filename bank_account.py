class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. Current balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}. Current balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

def main():
    account = BankAccount()
    
    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
