# Opis skryptów testowych
Niniejszy dokument opisuje cztery skrypty testowe wykonane w JavaScript przy użyciu Selenium WebDriver. Skrypty testują podstawowe funkcjonalności stron internetowych: DuckDuckGo, Google, Wikipedia oraz Joinero.

## Użycie
Każdy skrypt jest samodzielnym plikiem i można go uruchomić w środowisku Node.js, wywołując polecenie:
```bash
node nazwa_skryptu.js
```


## 1. Skrypt testujący DuckDuckGo
**test_duckduckgo.js**

Skrypt testuje funkcję wyszukiwania na stronie DuckDuckGo. Skrypt sprawdza, czy:
- Strona DuckDuckGo otwiera się poprawnie,
- Wyszukiwanie frazy "Polsko-Japońska Akademia Technik Komputerowych w Gdańsku" działa,
- Wyniki wyszukiwania zawierają odpowiednie elementy,
- Pierwszy wynik wyszukiwania zawiera słowo "Akademia" lub "PJATK".

Kroki:
- Przejście na stronę DuckDuckGo.
- Sprawdzenie tytułu strony.
- Wpisanie frazy w pole wyszukiwania.
- Oczekiwanie na załadowanie wyników.
- Sprawdzenie tytułu wyników.
- Weryfikacja obecności wyników.
- Sprawdzenie treści pierwszego wyniku.
- Wydruk komunikatu o zakończeniu testu.


## 2. Skrypt testujący Google
**test_google.js**

Skrypt testuje wyszukiwanie na Google, sprawdzając:
- Poprawność otwarcia strony Google,
- Wyszukiwanie frazy "Selenium WebDriver",
- Obecność wyników wyszukiwania,
- Czy wyniki wyszukiwania zawierają frazę "Selenium".

Kroki:
- Przejście na stronę Google.
- Zaakceptowanie polityki prywatności (jeśli jest obecna).
- Sprawdzenie tytułu strony.
- Wpisanie frazy w pole wyszukiwania i potwierdzenie Enterem.
- Oczekiwanie na wyniki.
- Sprawdzenie tytułu wyników.
- Weryfikacja obecności wyników.
- Weryfikacja adresu URL pod kątem frazy "Selenium".


## 3. Skrypt testujący Wikipedię
**test_wikipedia.js**

Skrypt testuje wyszukiwanie i nawigację na stronie Wikipedii, sprawdzając:
- Poprawność otwarcia strony,
- Wyszukiwanie frazy "Selenium",
- Obecność sekcji z wynikami oraz poprawność linków wewnętrznych.

Kroki:
- Przejście na stronę Wikipedia.
- Sprawdzenie tytułu strony.
- Wpisanie frazy w pole wyszukiwania.
- Oczekiwanie na załadowanie artykułu.
- Sprawdzenie obecności słowa "chemical" w treści artykułu.
- Znalezienie pierwszego linku w artykule i kliknięcie go.
- Sprawdzenie tytułu nowej strony.
- Weryfikacja obecności słowa "element" na nowej stronie.

## 4. Skrypt testujący Joinero
**test_joinero.js**

Skrypt testuje proces wyszukiwania i dodawania produktu do koszyka w sklepie Joinero.
- Poprawność otwarcia strony,
- Funkcję wyszukiwania,
- Dodanie produktu do koszyka oraz aktualizację liczby produktów w koszyku.

Kroki:
- Przejście na stronę Joinero.
- Sprawdzenie tytułu strony.
- Wyszukanie produktu za pomocą pola wyszukiwania.
- Wpisanie litery "a" w polu wyszukiwania.
- Oczekiwanie na sugestie wyszukiwania.
- Wybranie pierwszej sugestii.
- Znalezienie i kliknięcie przycisku "Dodaj do koszyka".
- Sprawdzenie liczby produktów w koszyku.







