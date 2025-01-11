"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

    with open('./files/input/data.csv', mode='r', encoding='utf-8') as f:
        data = f.readlines()

        for line in data:
            print(line.split()[1])

        letras = sorted(set([line.split()[0] for line in data]))
        dict_conteo = dict()
        for letra in letras:
            dict_conteo[letra] = 0
        list(map(lambda fila: dict_conteo.update({fila.split()[0]: dict_conteo[fila.split()[0]] + int(fila.split()[1])}), data))
        

        return list(dict_conteo.items())

