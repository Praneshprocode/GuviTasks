#Bank Account task

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.__balance = balance  # Encapsulation

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        return interest


class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, minimum_balance):
        super().__init__(account_number, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.get_balance() - amount >= self.minimum_balance:
            # Accessing protected operation through parent method logic
            current_balance = self.get_balance()
            new_balance = current_balance - amount

            # Name mangling to update private variable
            self._BankAccount__balance = new_balance
            print(f"Withdrawn: {amount}")
        else:
            print("Withdrawal denied! Minimum balance requirement violated.")


# Driver Code
print("=== Savings Account ===")
sa = SavingsAccount("SA101", 10000, 5)
sa.deposit(2000)
sa.withdraw(1500)
print("Balance:", sa.get_balance())
print("Interest:", sa.calculate_interest())

print("\n=== Current Account ===")
ca = CurrentAccount("CA201", 5000, 1000)
ca.withdraw(3500)
print("Balance:", ca.get_balance())
ca.withdraw(1000)