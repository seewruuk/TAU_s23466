# bank_system.py
import asyncio

class InsufficientFundsError(Exception):
    """Wyjątek zgłaszany, gdy na koncie nie ma wystarczających środków."""
    pass

class Account:
    def __init__(self, account_number: str, owner: str, balance: float = 0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        """Dodaje środki na konto."""
        if amount < 0:
            raise ValueError("Nie można wpłacić ujemnej kwoty.")
        self.balance += amount

    def withdraw(self, amount: float):
        """
        Wypłaca środki z konta.
        Jeśli saldo jest niewystarczające, podnosi InsufficientFundsError.
        """
        if amount < 0:
            raise ValueError("Nie można wypłacić ujemnej kwoty.")
        if self.balance < amount:
            raise InsufficientFundsError("Niewystarczające środki na koncie.")
        self.balance -= amount

    async def transfer(self, to_account: 'Account', amount: float):
        """
        Asynchroniczny transfer środków na inne konto.
        Symulujemy tu opóźnienie,
        a następnie wykonujemy withdraw() i deposit().
        """
        # Symulacja opóźnienia w transferze (np. zewnętrzna autoryzacja)
        await asyncio.sleep(0.1)
        self.withdraw(amount)
        to_account.deposit(amount)

class Bank:
    def __init__(self):
        # klucz: numer konta, wartość: obiekt Account
        self.accounts = {}

    def create_account(self, account_number: str, owner: str, initial_balance: float = 0.0):
        """
        Tworzy konto bankowe o podanym numerze konta, jeśli jeszcze nie istnieje.
        """
        if account_number in self.accounts:
            raise ValueError(f"Konto o numerze {account_number} już istnieje.")
        new_account = Account(account_number, owner, initial_balance)
        self.accounts[account_number] = new_account
        return new_account

    def get_account(self, account_number: str) -> Account:
        """Zwraca konto o podanym numerze, jeśli istnieje."""
        account = self.accounts.get(account_number)
        if not account:
            raise ValueError(f"Nie znaleziono konta o numerze {account_number}.")
        return account

    async def process_transaction(self, transaction_func):
        """
        Procesuje transakcję – np. wywołuje asynchroniczną funkcję transferu.
        Symulujemy również delikatne opóźnienie (np. weryfikacja w zewnętrznym systemie).
        """
        await asyncio.sleep(0.1)
        await transaction_func()
