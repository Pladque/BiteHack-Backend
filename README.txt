searchengine.cpp odpowiada za wyszukiwanie najbardziej podobnych do dodawanego wpisu pozycji w archiwum

URUCHOMIENIE:

program odpalamy nastepujaco (pod windowsem):

searchengine.exe plik1.txt plik2.txt a b

GDZIE:

- plik1 to dowolny plik tekstowy (rozszerzenia txt, in, out) zawierajacy wejscie do programu postaci:

tag1 tag2 tag3	//tagi dodawanego wpisu oddzielone pojedyncza spacja, po ostatnim nalezy dac tylko i wylacznie enter
slowo1 slowo2 slowo3	//tresc dodawanego wpisu w postaci slow z malych liter lub cyfr bez znakow specjalnych, oddzielonych spacja, po ostatnim jeden enter
	//Od nastepnej linii kazdy wpis, ktory byl juz w archiwum zostaje zapisany taka sama metoda jak dodawany wpis powyzej
	//Czyli: tagi oddzielone spacjami, enter, slowa oddzielone spacjami, enter


- plik 2 to dowolny plik tekstowy (rozszerzenia txt, in, out) do ktorego program wypisuje wynik:
wynik jest postaci jednej liczby na linie, oznaczajacej wpis ktory powinien znalezc sie na stronie
liczby te sa wypisane od najwazniejszego wpisu do najmniej waznego
liczba oznacza ktory z kolei byl ten wpis w pliku wejsciowym


- "a" to zmienna liczbowa oznaczajaca tryb pracy wyszukiwania:
Tryb 1 oznacza, ze szukamy najpierw po tagach, potem po slowach
Tryb 2 oznacza, ze szukamy najpierw po slowach, potem po tagach

- "b" to zmienna liczbowa oznaczajaca ile maksymalnie rekordow ma zwrocic wyszukiwarka
jezeli ustawimy "b" na 0 to nic sie nie wyswietli xd
w przypadku gdy mozliwych rekordow jest mniej niz "b" to nie uzupelnia tego niczym