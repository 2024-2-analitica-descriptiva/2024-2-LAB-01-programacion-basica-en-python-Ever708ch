"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    x = open(r'files\input\data.csv').readlines()
    x = [i.split("\t") for i in x]
    x = [int(i[1]) for i in x]
    x = sum(x)

    return x



"""
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
