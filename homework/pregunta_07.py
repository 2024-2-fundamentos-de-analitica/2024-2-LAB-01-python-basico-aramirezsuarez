def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
    file_path = './files/input/data.csv'
    try:
        with open(file_path, 'r') as file:
            data = file.readlines()

        # Diccionario para almacenar las letras asociadas a cada valor de la columna 2
        value_to_letters = {}

        for line in data:
            parts = line.strip().split('\t')
            letter = parts[0]
            value = int(parts[1])

            if value not in value_to_letters:
                value_to_letters[value] = []
            value_to_letters[value].append(letter)

        # Convertir el diccionario en una lista de tuplas y ordenar
        result = sorted(
            [(value, letters) for value, letters in value_to_letters.items()]
        )

        return result

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {file_path}")
        return []

    except Exception as e:
        print(f"Se produjo un error: {e}")
        return []
