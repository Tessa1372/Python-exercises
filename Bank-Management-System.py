from datetime import datetime
from dataclasses import dataclass
from typing import List, Dict

@dataclass #decorator
class Transaction_details:
    time: datetime
    transaction_method: str
    amount: float
    balance_after: float  

class Account:
    def __init__(self, account_number: str, name: str, contact_details: dict, balance: float = 0.0):
        self.account_number = account_number
        self.name = name
        self.contact_details = contact_details  
        self.balance = balance
        self.transactions: List[Transaction_details] = []
        if balance > 0:
            self.transactions.append(Transaction_details(datetime.now(), "INITIAL_DEPOSIT", balance, balance))

    def deposit(self, amount: float) -> bool:
        if not isinstance(amount, (int, float)):
            print("Invalid amount type. Please enter a number.")
            return False
        elif amount <= 0:
            print("Deposit should be a positive value")
            return False  

        self.balance += amount
        self.transactions.append(Transaction_details(datetime.now(), "DEPOSIT", amount, self.balance))
        print(f"Rs {amount:.3f} deposited successfully.") 
        return True

    def withdrawal(self, amount: float) -> bool:  
        if not isinstance(amount, (int, float)):
            print("Invalid amount type. Please enter a number.")
            return False
        elif amount <= 0:
            print("Withdrawal amount should be a positive value")
            return False 
        elif amount > self.balance:
            print("Insufficient balance.")
            return False

        self.balance -= amount
        self.transactions.append(Transaction_details(datetime.now(), "WITHDRAWAL", -amount, self.balance))
        print(f"Rs {amount:.3f} withdrawn successfully.")
        return True

    def balance_get(self) -> float:
        return self.balance

    def account_statement(self):  
        print("\n----Account Statement----")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Contact Details:")
        print(f"  Phone: {self.contact_details['phone']}")  
        print("\n----Transaction History----")
        print("Timestamp               Type         Amount     Balance")
        print("-" * 70)
        for transaction in self.transactions:
            print(f"{transaction.time.strftime('%Y-%m-%d %H:%M:%S')} {transaction.transaction_method:11} Rs {transaction.amount:9.3f} Rs {transaction.balance_after:9.3f}")
        print("-" * 70)
        print(f"Current Balance: Rs {self.balance:.3f}")

class Bank:
    def __init__(self):
        self.accounts: Dict[str, Account] = {}

    def validate_account_number(self, account_number: str) -> bool:
        return account_number.isalnum() and 5 <= len(account_number) <= 10

    def validate_contact(self, email: str, phone: str) -> bool:
        if not phone.isdigit() or len(phone) != 10:
            print("Invalid phone number. Please enter 10 digits.")
            return False
        return True

    def create_account(self, account_number: str, name: str, contact: dict, initial_deposit: float = 0.0) -> bool:
        if not self.validate_account_number(account_number):
            print("Invalid account number.")
            return False
            
        if account_number in self.accounts:
            print("Account number already exists.")
            return False
            
        if not name.strip():
            print("Name cannot be empty.")
            return False
            
        if not self.validate_contact(contact['email'], contact['phone']):
            return False
            
        if initial_deposit < 0:
            print("Initial deposit cannot be negative.")
            return False

        account = Account(account_number, name, contact, initial_deposit)
        self.accounts[account_number] = account
        print("Account created successfully.")
        return True

    def get_account(self, account_number: str) -> Account:  
        account = self.accounts.get(account_number)
        if not account:
            print("Account not found.")
        return account

    def display_all_accounts(self) -> None:  
        if not self.accounts:
            print("No accounts in the bank.")
            return
            
        print("\n=== All Bank Accounts ===")
        for account in self.accounts.values():
            print(f"\nAccount Number: {account.account_number}")
            print(f"Account Holder: {account.name}")
            print(f"Email: {account.contact_details['email']}")  
            print(f"Phone: {account.contact_details['phone']}")  
            print(f"Balance: Rs {account.balance:.2f}")
            print("-" * 30)

def get_valid_float_input(prompt: str) -> float: 
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    bank = Bank()

    while True:
        print("\n=== Welcome to the ABC Bank ===")
        print("1. Create Account")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Generate Account Statement")
        print("5. Display All Accounts")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            account_number = input("Enter account number (5-10 alphanumeric characters): ")
            name = input("Enter customer name: ")
            email = input("Enter email address: ")
            phone = input("Enter phone number (10 digits): ")
            initial_deposit = get_valid_float_input("Enter initial deposit amount: ")
            
            contact = {'email': email, 'phone': phone}
            bank.create_account(account_number, name, contact, initial_deposit)

        elif choice == '2':
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)  
            if account:
                amount = get_valid_float_input("Enter deposit amount: ")
                account.deposit(amount)

        elif choice == '3':
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)  
            if account:
                amount = get_valid_float_input("Enter withdrawal amount: ")
                account.withdrawal(amount)  

        elif choice == '4':
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)  
            if account:
                account.account_statement() 

        elif choice == '5':
            bank.display_all_accounts()

        elif choice == '6':
            print("Thank you for using ABC Bank!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
