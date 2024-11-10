# Opis skryptów testowych
Niniejszy dokument opisuje cztery skrypty testowe wykonane w JavaScript przy użyciu Selenium WebDriver. Skrypty testują podstawowe funkcjonalności stron internetowych: DuckDuckGo, Google, Wikipedia oraz Joinero.

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



