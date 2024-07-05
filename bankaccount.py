class Account:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.__account_number = account_number
        self.__balance = balance
    
    def add_balance(self, amount):
        self.__balance += amount
        return f"Deposited Amount: {amount}. Total Amount: {self.__balance}"
    
    def withdraw(self, amount):
        if self.__balance - amount >= 100:
            self.__balance -= amount
            return f"Withdrawal Amount: {amount}. Total Amount: {self.__balance}"
        else:
            return "Insufficient Balance! ."
    
    def view_balance(self):
        return f"Total Balance: {self.__balance} Rupees"
    
    def info(self):
        return f"Name: {self.name}, Account Number: {self.__account_number}, Balance: {self.__balance}"

name = input("Enter You Name Here:-")
number = input("Enter Account Number Here:-")
balance = float(input("Enter First Balance To Add:-"))
account = Account(name,number,balance)

while True:
    print("\n---Bank Account Code---")
    print("1. Add Amount")
    print("2. Withdraw Amount")
    print("3. View Balance")
    print("4. Account Information")
    print("5. Exit")

    choice = (input("Enter your choice between 1-5:- "))
    if choice =='1':
        balance = int(input("Enter Amount to add:- "))
        print(account.add_balance(balance))
    elif choice =='2':
        amount = int(input("Enter amount to withdraw:- "))
        print(account.withdraw(amount))
    elif choice == '3':
        print(account.view_balance())
    elif choice =='4':
        print(account.info())
    elif choice =='5':
        print("Exit......")
        break
    else:
        print("Error!")
