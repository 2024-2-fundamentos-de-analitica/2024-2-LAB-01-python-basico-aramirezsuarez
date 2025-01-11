def pregunta_10():
    """
    Retorne una lista de tuplas que contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]
    """
    file_path = "./files/input/data.csv"
    try:
        # Abrimos y leemos el archivo
        with open(file_path, "r", encoding="utf-8") as file:
            data = file.readlines()

        # Crear una lista para almacenar el resultado
        result = []

        # Procesar cada línea
        for line in data:
            try:
                # Separar las columnas
                columns = line.strip().split("\t")
                letter = columns[0]  # Columna 1 (letra)
                col4_elements = len(columns[3].split(","))  # Cantidad de elementos en la columna 4
                col5_elements = len(columns[4].split(","))  # Cantidad de elementos en la columna 5

                # Añadir la tupla (letra, elementos en col 4, elementos en col 5) al resultado
                result.append((letter, col4_elements, col5_elements))
            except IndexError as e:
                print(f"Error al procesar la línea: {line.strip()}. Detalle: {e}")
                continue

        return result

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {file_path}")
        return []

    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
        return []

