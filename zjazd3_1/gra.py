"""
TAU zjazd 3
Autor: Kacper Sewruk s23466
"""

import random

class Gra:
    """
    Klasa reprezentująca grę.

    Atrybuty:
        szerokosc (int): Szerokość planszy (minimalnie 5).
        wysokosc (int): Wysokość planszy (minimalnie 5).
        plansza (list): Dwuwymiarowa lista reprezentująca planszę gry.
        pozycja_start (tuple): Współrzędne punktu START.
        pozycja_stop (tuple): Współrzędne punktu STOP.
        pozycja_gracza (tuple): Aktualne współrzędne gracza.
        wygrana (bool): Flaga oznaczająca zakończenie gry wygraną.
    """

    def __init__(self, szerokosc=5, wysokosc=5):
        """
        Inicjalizuje nową grę, generuje planszę, pozycje START i STOP oraz przeszkody.

        Args:
            szerokosc (int, opcjonalnie): Szerokość planszy. Domyślnie 5.
            wysokosc (int, opcjonalnie): Wysokość planszy. Domyślnie 5.
        """
        self.szerokosc = max(5, szerokosc)
        self.wysokosc = max(5, wysokosc)
        self.plansza = [[' ' for _ in range(self.szerokosc)] for _ in range(self.wysokosc)]
        self.pozycja_start = None
        self.pozycja_stop = None
        self.pozycja_gracza = None
        self.generuj_pozycje_start_stop()
        self.generuj_przeszkody()
        self.pozycja_gracza = self.pozycja_start
        self.wygrana = False

    def generuj_pozycje_start_stop(self):
        """
        Generuje losowe pozycje START i STOP na krawędziach planszy, upewniając się, że nie są sąsiadami.
        """
        pozycje_krawedziowe = []
        for x in range(self.szerokosc):
            pozycje_krawedziowe.append((0, x))
            pozycje_krawedziowe.append((self.wysokosc - 1, x))
        for y in range(1, self.wysokosc -1):
            pozycje_krawedziowe.append((y, 0))
            pozycje_krawedziowe.append((y, self.szerokosc - 1))
        self.pozycja_start = random.choice(pozycje_krawedziowe)
        pozycje_krawedziowe.remove(self.pozycja_start)
        sasiedzi = self.sasiednie_pola(self.pozycja_start[0], self.pozycja_start[1])
        pozycje_krawedziowe = [p for p in pozycje_krawedziowe if p not in sasiedzi]
        self.pozycja_stop = random.choice(pozycje_krawedziowe)
        self.plansza[self.pozycja_start[0]][self.pozycja_start[1]] = 'A'
        self.plansza[self.pozycja_stop[0]][self.pozycja_stop[1]] = 'B'

    def generuj_przeszkody(self):
        """
        Losowo generuje przeszkody na planszy, oznaczane jako 'X', zapełniając około 20% planszy.
        """
        liczba_przeszkod = (self.szerokosc * self.wysokosc) // 5  # np. 20% planszy to przeszkody
        for _ in range(liczba_przeszkod):
            x = random.randint(0, self.wysokosc -1)
            y = random.randint(0, self.szerokosc -1)
            if self.plansza[x][y] == ' ':
                self.plansza[x][y] = 'X'

    def sasiednie_pola(self, x, y):
        """
        Zwraca listę współrzędnych sąsiadujących pól dla podanej pozycji.

        Args:
            x (int): Współrzędna X pola.
            y (int): Współrzędna Y pola.

        Returns:
            list: Lista krotek reprezentujących sąsiadujące pola.
        """
        pola = []
        if x > 0:
            pola.append((x -1, y))
        if x < self.wysokosc -1:
            pola.append((x +1, y))
        if y > 0:
            pola.append((x, y -1))
        if y < self.szerokosc -1:
            pola.append((x, y +1))
        return pola

    def ruch(self, kierunek):
        """
        Przesuwa gracza w podanym kierunku, jeśli ruch jest dozwolony.

        Args:
            kierunek (str): Kierunek ruchu ('gora', 'dol', 'lewo', 'prawo').

        Returns:
            bool: True jeśli ruch się powiódł, False w przeciwnym razie.
        """
        if self.wygrana:
            return False
        x, y = self.pozycja_gracza
        if kierunek == 'gora':
            x -=1
        elif kierunek == 'dol':
            x +=1
        elif kierunek == 'lewo':
            y -=1
        elif kierunek == 'prawo':
            y +=1
        else:
            print("Nieznany kierunek!")
            return False

        if not (0 <= x < self.wysokosc and 0 <= y < self.szerokosc):
            print("Nie można wyjść poza planszę!")
            return False
        if self.plansza[x][y] == 'X':
            print("Na drodze jest przeszkoda!")
            return False
        if self.pozycja_gracza != self.pozycja_start:
            self.plansza[self.pozycja_gracza[0]][self.pozycja_gracza[1]] = ' '
        self.pozycja_gracza = (x, y)
        if self.pozycja_gracza == self.pozycja_stop:
            print("Dotarłeś do mety!")
            self.wygrana = True
            self.plansza[x][y] = 'A'
        else:
            self.plansza[x][y] = 'A'
        return True

    def wyswietl_plansze(self):
        """
        Wyświetla aktualny stan planszy w terminalu.
        """
        for wiersz in self.plansza:
            print(' '.join(wiersz))

if __name__ == "__main__":
    gra = Gra(5, 5)
    gra.wyswietl_plansze()
    print("\n--- Test ruchów ---\n")

    ruchy = ['gora', 'dol', 'lewo', 'prawo', 'gora', 'gora']

    for ruch in ruchy:
        print(f"Ruch w kierunku: {ruch}")
        wynik = gra.ruch(ruch)
        gra.wyswietl_plansze()
        print("\n")
        if gra.wygrana:
            print("Gra zakończona sukcesem!")
            break
