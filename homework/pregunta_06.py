"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    x = open('files\input\data.csv').readlines()
    x = [i.split() for i in x]
    x = [i[4].split(",") for i in x]

    new_data = []

    for i in x:
        elements = []
        for j in i:
            key, value = j.split(":") 
            elements.append([key, int(value)]) 
        new_data.append(elements)
    merged_data = [item for sublist in new_data for item in sublist]
    
    group = {}    
    for key, value in merged_data:
        value = int(value)
        if key in group:
            group[key].append(value)
        else:
            group[key] = [value]
    x = [(key, min(value), max(value)) for key, value in group.items()]
    x.sort()
    return x
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
