# -*- coding: utf-8 -*-

import numpy as np


def linear_func(x, a, b):
    """
    Funkcja ta zwraca a*x + b, funkcja ta powinna działać bez względu
    na to czy x to tablica numpy czy liczba zmiennoprzecinkowa.

    Podpowiedź: Nie jest to bardzo trudne.

    :param np.ndarray x:
    :param float a:
    :param float b:
    """
    return a*x + b

def chisquared(xy, a, b):
    """

    Funkcja liczy sumę Chi^2 między wartościami zmierzonej funkcji a funkcją 
    liniową o wzorze a*x + b.

    Sumę chi^2 definiujemy jako:

    Chi^2 = Sum(( (y - f(x))/sigma_y)^2)

    gdzie f(x) to w naszym przypadku funkcja liniowa


    :param np.ndarray xy: Tablica o rozmiarze N x 3, w pierwszej kolumnie
    zawarte są wartości zmiennej a w drugiej wartości y.
    :param float a:
    :param float b:
    :return:
    """
    chi2 = np.sum( (xy[:,1] - linear_func(xy[:,0], a, b)) * (xy[:,1] - linear_func(xy[:,0], a, b)) / xy.shape[0])
    return chi2

def least_sq(xy):
    """
    Funkcja liczy parametry funkcji liniowej ax+b do danych za pomocą metody
    najmniejszych kwadratów.

    A = (Sum(x^2)*Sum(y)-Sum(x)*Sum(xy))/Delta
    B = (N*Sum(xy)-Sum(x)*Sum(y))/Delta
    Delta = N*Sum(x^2) - (Sum(x)^2)

    :param xy: Jak w chisquared, uwaga: sigma_y nie jest potrzebne.
    :return: Krotka
    """
    N = xy.shape[0]
    Delta = N * np.sum(xy[:,0] * xy[:,0]) - np.sum(xy[:,0]) * np.sum(xy[:,0])
    A = (np.sum(xy[:,0] * xy[:,0]) * np.sum(xy[:,1]) - np.sum(xy[:,0]) * np.sum(xy[:,0] * xy[:,1])) / Delta
    B = (N * np.sum(xy[:,0] * xy[:,1]) - np.sum(xy[:,0]) * np.sum(xy[:,1])) / Delta
    return (A, B)
