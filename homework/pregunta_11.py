"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    x = open('files\input\data.csv').readlines()
    x = [line.strip().split('\t') for line in x]
    x1 = [int(i[1]) for i in x]
    x2 = [i[3].split(',') for i in x]    
    key_value = list(zip(x2, x1))

    keys = []
    for x in x2:
        keys.extend(x)
    dict_keys = sorted(set(keys))

    dic=dict()
    for key in dict_keys:
        dic[key] = 0

    for x,y in key_value:
        for i in x:
            dic[i]+= y
 
    return dic
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
