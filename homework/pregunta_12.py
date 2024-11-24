"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    x = open('files/input/data.csv', 'r').readlines()
    x = [line.strip().split('\t') for line in x]
    x1 = [i[0] for i in x]
    x5 = [i[4].split(',') for i in x]
    key_value = list(zip(x1,x5))
    keys = sorted(set(x1))

    dic = dict()
    for key in keys:
        dic[key] = 0

    for x,y in key_value:
        for i in y:
            dic[x]+= int(i[4:])
 
    return dic
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
