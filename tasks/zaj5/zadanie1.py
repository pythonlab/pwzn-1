# -*- coding: utf-8 -*-
from numpy import char

import numpy as np
import mmap

def next_item(input):
    """
    Zwraca "następny" ngram dla podanego n-gramu. Działa to dla ciągów znaków ASCII.
    To jest hak, ale działa.

    Można zaimplementować to lepiej.
    :param input:
    :return:
    """
    return input[:-1] + chr(ord(input[-1])+1)


def load_data(path):
    """
    Funkcja która ładuje dane z pliku zawierającego ngramy. Plik ten jest
    plikiem binarnym zawierającym N wierszy. W każdym wierszu jest 7 bajtów 
    zawierających 7-gram a następnie czterobajtowa liczba całkowita zawierająca
    ilość zliczeń.

    Funkcja zwraca tablicę numpy. Tablica ta jest tylko do odczytu.

    Podpowiedź: starczą dwie linijki kodu definicja dtype oraz otwarcie macierzy.
    Typ danych jest złożony --- należy użyć Structured Array.
    """
    dtype = np.dtype([
            ("7-gram", np.dtype("a7")),
            ("counts", np.dtype("u4"))])

    data = np.memmap(path, dtype=dtype)
    return data

def suggester(input, data):
    """
    Funkcja która sugeruje następną literę ciągu ``input`` na podstawie n-gramów
    zawartych w ``data``.

    :param str input: Ciąg znaków o długości 6 znaków. **UWAGA** Na zajęciach trzecich
                      input mógł mieć dowolną długość.
    :param np.ndarray data: Wynik działania ``load_data``.
    :return: Dowolną strukturę którą można zaindeksować w następujący sposób:
            ret[0][0] zwraca najbardziej prawdopodobną następną literę. ret[0][1]
            jej prawdopodobieństwo. ret[-1][0] zwraca najmniej prawdopodobną literę.
            Dane posortowane są względem prawdopodobieństwa.

    By wygenerować częstotliwości należy:

    Dla ustalenia uwagi zakładamy ze input zawiera ciąg znaków `foo`

    1. Znaleźć "następny" n-gram. Krótka funkcja "hak", która zwraca następny
       n-gram jest z
    2. Odnaleźć pierwsze i ostatnie wystąpienie ngramu rozpoczynającego się od wartości
       ``foo``.
    3. Wyznaczyć prawdopodobieństwo wystąpienia kolejnej litery, posortować i zwrócić.

    Przykład zastosowania:

    >>> data = load_data("path")
    >>> suggester('ąęćś', data)
    []
    >>> suggester('pytho', data)
    [('n', 1.0)]
    >>> suggester('pytho', data)
    [('o', 0.7794117647058824),
     ('a', 0.1323529411764706),
     ('e', 0.07352941176470588),
     ('i', 0.014705882352941176)]
    """
    next_input = next_item(input)
    first_index, second_index = np.searchsorted(data['7-gram'], [input, next_input])
    array = data[first_index:second_index]
    n = array.shape
    dict = {}
    N=0
    for ii in range(n[0]):
        letter, value = array[ii]
        N+=value
        if letter not in dict:
            dict[letter] = value
        elif letter in dict:
            dict[letter] += value
        
    list=[]
    for key, value in dict.items():
        value = value / N
        letter = key[-1]
        tuple = (chr(letter), value)
        list.append(tuple)
 
    list.sort(key=lambda x: -x[1])
    return list

# data = load_data("enwiki-20140903-pages-articles_part_0.xmlascii1000.bin")
# list = suggester('pytho', data)
# print(list)
