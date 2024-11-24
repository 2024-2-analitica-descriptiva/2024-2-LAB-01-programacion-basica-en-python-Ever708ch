"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    x = open('files/input/data.csv', 'r').readlines()
    x1 = [i.split()[0].split(",") for i in x]
    x2 = [len(i.split()[3].split(",")) for i in x]
    x3 = [len(i.split()[4].split(",")) for i in x]
    list_1 = list(zip(x1, x2, x3))
    list_2 = [(letra[0], num1, num2) for letra, num1, num2 in list_1]

    return list_2
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
