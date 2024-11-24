"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    from collections import Counter
    x = open('files\input\data.csv', "r").readlines()
    x = [i.split()[4].split(",") for i in x]
    group = []
    for row in x:
        for item in row:
            key, value = item.split(":")
            value = int(value)
            group.append(key)
    letters = dict(sorted(list(Counter(group).items())))

    return letters
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
