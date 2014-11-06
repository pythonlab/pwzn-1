# -*- coding: utf-8 -*-

import csv

def merge(path1, path2, out_file):
    """
    Funkcja pobiera nazwy dwóch plików z n-gramami (takie jak w poprzedmim
    zadaniu) i łączy zawartość tych plików i zapisuje do pliku w ścieżce ``out``.

    Pliki z n-gramami są posortowane względem zawartości n-grama.

    :param str path1: Ścieżka do pierwszego pliku
    :param str path2: Ścieżka do drugiego pliku
    :param str out_file:  Ścieżka wynikowa

    Testowanie tej funkcji na pełnych danych może być mało wygodne, możecie
    stworzyć inną funkcję która działa na dwóch listach/generatorach i testować
    ją.

    Naiwna implementacja polegałaby na stworzeniu dwóch słowników które
    zawierają mapowanie ngram -> ilość wystąpień i połączeniu ich.

    Lepsza implementacja ładuje jeden z plików do pamięci RAM (jako słownik
    bądź listę) a po drugim iteruje.

    Najlepsza implementacja nie wymaga ma złożoność pamięciową ``O(1)``.
    Podpowiedź: merge sort. Nie jest to trywialne zadanie, ale jest do zrobienia.
    """
    list = []
    dict = {}
    with open(path1, 'r') as f:
        r = csv.reader(f, dialect=csv.unix_dialect)
        for line in r:
            #tuple = (line[0], int(line[1]))
            #list.append(tuple)
            dict[line[0]] = int(line[1])
    #for ii in list:
    #    dict[ii[0]] = int(ii[1])
    with open(path2, 'r') as f:
        r = csv.reader(f, dialect=csv.unix_dialect)
        for line in r:
            if line[0] in dict:
                dict[line[0]] += int(line[1])
            else:
                dict[line[0]] = int(line[1])
    list2 = []
    for key, value in dict.items():
        tuple = (key, value)
        list2.append(tuple)
    list2.sort(key=lambda x: x[0])
    with open(out_file, 'w') as f:
        w = csv.writer(f, dialect=csv.unix_dialect)
        w.writerows(list2)

if __name__ == '__main__':

    merge(
        '/opt/pwzn/zaj3/enwiki-20140903-pages-articles_part_0.xmlascii1000.csv',
        '/opt/pwzn/zaj3/enwiki-20140903-pages-articles_part_1.xmlascii1000.csv',
        '/tmp/mergeout.csv')
