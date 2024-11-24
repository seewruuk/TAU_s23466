import unittest
from gra import Gra

class TestGra(unittest.TestCase):
    def test_ruch_poza_plansze(self):
        """
        Testuje próbę ruchu poza granice planszy.
        """
        gra = Gra(5, 5)
        gra.pozycja_gracza = (0, 0)  # Ustawiamy gracza w lewym górnym rogu
        wynik = gra.ruch('gora')  # Próba ruchu poza planszę
        self.assertFalse(wynik)

    def test_ruch_na_przeszkode(self):
        """
        Testuje próbę ruchu na pole z przeszkodą.
        """
        gra = Gra(5, 5)
        gra.pozycja_gracza = (2, 2)
        gra.plansza[1][2] = 'X'  # Ustawiamy przeszkodę powyżej gracza
        wynik = gra.ruch('gora')  # Próba ruchu na przeszkodę
        self.assertFalse(wynik)

    def test_prawidlowy_ruch(self):
        """
        Testuje prawidłowy ruch gracza.
        """
        gra = Gra(5, 5)
        gra.pozycja_gracza = (2, 2)
        wynik = gra.ruch('gora')  # Prawidłowy ruch
        self.assertTrue(wynik)
        self.assertEqual(gra.pozycja_gracza, (1, 2))

    def test_wygrana(self):
        """
        Testuje czy gra rozpoznaje wygraną po dotarciu do pola STOP.
        """
        gra = Gra(5, 5)
        gra.pozycja_gracza = (1, 1)
        gra.pozycja_stop = (0, 1)
        gra.plansza[0][1] = 'B'
        wynik = gra.ruch('gora')  # Ruch na pole STOP
        self.assertTrue(wynik)
        self.assertTrue(gra.wygrana)

if __name__ == '__main__':
    unittest.main()
