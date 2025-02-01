# test_bank_system.py
import pytest
import asyncio
from unittest.mock import patch

from bank_system import Account, Bank, InsufficientFundsError

@pytest.fixture
def sample_bank():
    """
    Tworzy obiekt Bank wraz z dwoma kontami do celów testowych.
    Dzięki temu w testach nie trzeba za każdym razem tworzyć
    obiektów banku i kont od nowa.
    """
    bank = Bank()
    bank.create_account("123", "Alice", 1000.0)
    bank.create_account("456", "Bob", 500.0)
    return bank

def test_account_deposit():
    """Test poprawności wpłaty środków na konto."""
    acc = Account("111", "Test User", 100.0)
    acc.deposit(50.0)
    assert acc.balance == 150.0

    # Test wpłaty ujemnej kwoty
    with pytest.raises(ValueError):
        acc.deposit(-10)

def test_account_withdraw():
    """Test wypłaty środków z konta."""
    acc = Account("111", "Test User", 200.0)
    acc.withdraw(100.0)
    assert acc.balance == 100.0

    # Test próby wypłaty większej kwoty niż saldo
    with pytest.raises(InsufficientFundsError):
        acc.withdraw(200.0)

    # Test wypłaty ujemnej kwoty
    with pytest.raises(ValueError):
        acc.withdraw(-50.0)

@pytest.mark.asyncio
async def test_account_transfer():
    """Test asynchronicznego przelewu pomiędzy kontami."""
    acc1 = Account("111", "User1", 500.0)
    acc2 = Account("222", "User2", 300.0)

    await acc1.transfer(acc2, 200.0)
    assert acc1.balance == 300.0
    assert acc2.balance == 500.0

    # Próba przelewu większego niż stan konta
    with pytest.raises(InsufficientFundsError):
        await acc1.transfer(acc2, 1000.0)

@pytest.mark.asyncio
async def test_bank_create_and_get_account(sample_bank):
    """Test tworzenia i pobierania kont w klasie Bank."""
    # Sprawdź czy konta z fixture zostały poprawnie utworzone
    account_alice = sample_bank.get_account("123")
    assert account_alice.owner == "Alice"
    assert account_alice.balance == 1000.0

    account_bob = sample_bank.get_account("456")
    assert account_bob.owner == "Bob"
    assert account_bob.balance == 500.0

    # Tworzenie nowego konta
    new_acc = sample_bank.create_account("789", "Charlie", 250.0)
    assert new_acc.balance == 250.0
    assert new_acc.owner == "Charlie"

    # Próba stworzenia konta o istniejącym numerze
    with pytest.raises(ValueError):
        sample_bank.create_account("123", "SomeoneElse", 9999.0)

    # Próba pobrania nieistniejącego konta
    with pytest.raises(ValueError):
        sample_bank.get_account("999")

@pytest.mark.asyncio
async def test_bank_process_transaction(sample_bank):
    """Testujemy asynchroniczne przetwarzanie transakcji (process_transaction)."""
    account_alice = sample_bank.get_account("123")
    account_bob = sample_bank.get_account("456")

    async def transfer_func():
        await account_alice.transfer(account_bob, 200.0)

    await sample_bank.process_transaction(transfer_func)

    assert account_alice.balance == 800.0
    assert account_bob.balance == 700.0

@pytest.mark.asyncio
async def test_mocked_external_call(sample_bank):
    """
    Przykład mockowania: używamy patch do zastąpienia asyncio.sleep,
    aby nie spowalniać testów i sprawdzić, czy w ogóle jest wywoływany.
    """
    account_alice = sample_bank.get_account("123")
    account_bob = sample_bank.get_account("456")

    with patch("asyncio.sleep", return_value=None) as mock_sleep:
        await account_alice.transfer(account_bob, 100)
        mock_sleep.assert_called_once()  # sprawdzamy, czy asyncio.sleep zostało wywołane
        assert account_alice.balance == 900.0
        assert account_bob.balance == 600.0
