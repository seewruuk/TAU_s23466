# Laboratorium 6 – pyTest

Kacper Sewruk **s23466**

Projekt przedstawia prosty system bankowy do obsługi transakcji (wpłaty, wypłaty, przelewy) realizowanych asynchronicznie w języku Python. Zawiera również zestaw testów jednostkowych i asynchronicznych napisanych z wykorzystaniem **pytest** i **pytest-asyncio**.

## Zawartość

- **bank_system.py**  
  Zawiera klasy:
  - `Account` – reprezentuje konto bankowe (z metodami: `deposit`, `withdraw` i asynchronicznym `transfer`).
  - `Bank` – zarządza kontami (m.in. tworzenie kont, pobieranie, asynchroniczne `process_transaction`).
  - `InsufficientFundsError` – wyjątek zgłaszany przy niewystarczających środkach.

- **test_bank_system.py**  
  Zawiera testy (w tym asynchroniczne) sprawdzające funkcjonalność klas `Account` i `Bank`:
  - Test poprawności wpłaty i wypłaty (w tym wyjątków `InsufficientFundsError` i `ValueError`).
  - Test asynchronicznego transferu środków.
  - Test tworzenia i pobierania kont z klasy `Bank`.
  - Test asynchronicznego przetwarzania transakcji (`process_transaction`).
  - Przykład mockowania (np. `asyncio.sleep`) z wykorzystaniem **unittest.mock**.

- **pytest.ini** (opcjonalnie)  
  Plik konfiguracyjny dla pytest

- **requirements.txt** (opcjonalnie)  
  Lista bibliotek potrzebnych do uruchomienia testów (m.in. `pytest`, `pytest-asyncio`).


## Uruchomienie testów oraz wyniki

Aby uruchomić testy, należy zainstalować wymagane biblioteki (jeśli nie są zainstalowane) i uruchomić **pytest**:
   ```bash
   pytest   
```

Przykładowy wynik testów:
![img.png](img.png)





