def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera columna que aparecen asociadas a dicho valor de la segunda
    columna.
    
    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]
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
                value_to_letters[value] = set()  # Usamos un set para evitar duplicados
            value_to_letters[value].add(letter)

        # Convertir los sets en listas ordenadas
        result = sorted(
            [(value, sorted(list(letters))) for value, letters in value_to_letters.items()]
        )

        return result

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {file_path}")
        return []

    except Exception as e:
        print(f"Se produjo un error: {e}")
        return []