class BankAccount:
    def __init__(self, initial_balance=0):
        # Encapsulated attribute
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add money to the account balance."""
        self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw money if sufficient balance exists. Returns True/False."""
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display current balance with 2 decimal places."""
        print(f"Current Balance: ${self.account_balance:.2f}")


