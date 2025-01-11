def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    file_path = './files/input/data.csv'
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            data = f.readlines()

            maximo_minimo = [line.split()[0:2] for line in data]
            dict_results = {}

            for letra, value in maximo_minimo:
                value = int(value)
                if letra in dict_results:
                    dict_results[letra][0] = max(dict_results[letra][0], value)
                    dict_results[letra][1] = min(dict_results[letra][1], value)
                else:
                    dict_results[letra] = [value, value]

            return sorted((letra, valores[0], valores[1]) for letra, valores in dict_results.items())

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {file_path}")
        return []

    except ValueError as ve:
        print(f"Error al procesar los valores: {ve}")
        return []

    except Exception as e:
        print(f"Se produjo un error: {e}")
        return []
