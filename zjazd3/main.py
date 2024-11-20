import pygame
import random
import sys

# Inicjalizacja Pygame
pygame.init()

# Stałe
ROZMIAR_KRATKI = 40
KOLOR_TLA = (255, 255, 255)
KOLOR_SCIANY = (0, 0, 0)
KOLOR_START = (0, 255, 0)
KOLOR_STOP = (255, 0, 0)
KOLOR_GRACZ = (0, 0, 255)

class Gra:
    def __init__(self, szerokosc=5, wysokosc=5):
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

        # Ustawienia okna
        self.okno = pygame.display.set_mode((self.szerokosc * ROZMIAR_KRATKI, self.wysokosc * ROZMIAR_KRATKI))
        pygame.display.set_caption("Prosta Gra")
        self.okno.fill(KOLOR_TLA)

    def generuj_pozycje_start_stop(self):
        # Losowanie pozycji na krawędziach planszy
        pozycje_krawedziowe = []
        for x in range(self.szerokosc):
            pozycje_krawedziowe.append((0, x))
            pozycje_krawedziowe.append((self.wysokosc - 1, x))
        for y in range(1, self.wysokosc -1):
            pozycje_krawedziowe.append((y, 0))
            pozycje_krawedziowe.append((y, self.szerokosc - 1))
        self.pozycja_start = random.choice(pozycje_krawedziowe)
        pozycje_krawedziowe.remove(self.pozycja_start)
        # Usuwamy sąsiadujące pola
        sasiedzi = self.sasiednie_pola(self.pozycja_start[0], self.pozycja_start[1])
        pozycje_krawedziowe = [p for p in pozycje_krawedziowe if p not in sasiedzi]
        self.pozycja_stop = random.choice(pozycje_krawedziowe)
        self.plansza[self.pozycja_start[0]][self.pozycja_start[1]] = 'A'
        self.plansza[self.pozycja_stop[0]][self.pozycja_stop[1]] = 'B'

    def generuj_przeszkody(self):
        liczba_przeszkod = (self.szerokosc * self.wysokosc) // 5  # np. 20% planszy to przeszkody
        for _ in range(liczba_przeszkod):
            x = random.randint(0, self.wysokosc -1)
            y = random.randint(0, self.szerokosc -1)
            if self.plansza[x][y] == ' ':
                self.plansza[x][y] = 'X'

    def sasiednie_pola(self, x, y):
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
        if self.wygrana:
            return
        x, y = self.pozycja_gracza
        if kierunek == 'gora':
            x -=1
        elif kierunek == 'dol':
            x +=1
        elif kierunek == 'lewo':
            y -=1
        elif kierunek == 'prawo':
            y +=1

        if not (0 <= x < self.wysokosc and 0 <= y < self.szerokosc):
            # Wyjście poza planszę
            return
        if self.plansza[x][y] == 'X':
            # Na drodze jest przeszkoda
            return
        # Aktualizacja pozycji gracza
        self.pozycja_gracza = (x, y)
        if self.pozycja_gracza == self.pozycja_stop:
            print("Dotarłeś do mety!")
            self.wygrana = True

    def rysuj_plansze(self):
        for i in range(self.wysokosc):
            for j in range(self.szerokosc):
                x = j * ROZMIAR_KRATKI
                y = i * ROZMIAR_KRATKI
                rect = pygame.Rect(x, y, ROZMIAR_KRATKI, ROZMIAR_KRATKI)
                if self.plansza[i][j] == 'X':
                    pygame.draw.rect(self.okno, KOLOR_SCIANY, rect)
                elif (i, j) == self.pozycja_start:
                    pygame.draw.rect(self.okno, KOLOR_START, rect)
                elif (i, j) == self.pozycja_stop:
                    pygame.draw.rect(self.okno, KOLOR_STOP, rect)
                else:
                    pygame.draw.rect(self.okno, KOLOR_TLA, rect)
                pygame.draw.rect(self.okno, KOLOR_SCIANY, rect, 1)

        # Rysowanie gracza
        x = self.pozycja_gracza[1] * ROZMIAR_KRATKI
        y = self.pozycja_gracza[0] * ROZMIAR_KRATKI
        rect = pygame.Rect(x, y, ROZMIAR_KRATKI, ROZMIAR_KRATKI)
        pygame.draw.rect(self.okno, KOLOR_GRACZ, rect)

    def uruchom(self):
        clock = pygame.time.Clock()
        while True:
            self.okno.fill(KOLOR_TLA)
            self.rysuj_plansze()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.ruch('gora')
                    elif event.key == pygame.K_DOWN:
                        self.ruch('dol')
                    elif event.key == pygame.K_LEFT:
                        self.ruch('lewo')
                    elif event.key == pygame.K_RIGHT:
                        self.ruch('prawo')
            clock.tick(30)

# Przykładowe użycie
if __name__ == "__main__":
    gra = Gra(10, 10)
    gra.uruchom()
