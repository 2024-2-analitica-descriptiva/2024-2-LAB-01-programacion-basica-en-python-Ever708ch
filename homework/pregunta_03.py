"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    x = open('files/input/data.csv', 'r').readlines()
    x = [i[0:3] for i in x]
    x = [i.split() for i in x]
    acumulador = {}
    for key, value in x:
        value = int(value)
        if key in acumulador:
            acumulador[key] += value
        else:
            acumulador[key] = value

    resultado = sorted(acumulador.items())
    return resultado
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
