"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    x = open('files/input/data.csv', 'r').readlines()
    group = {}
    x = [i[0:3].split("\t") for i in x]
    for key, value in x:
        value = int(value)
        if key in group:
            group[key].append(value)
        else:
            group[key] = [value]
    x = [(key, max(value), min(value)) for key, value in group.items()]
    x.sort()
    return x
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
