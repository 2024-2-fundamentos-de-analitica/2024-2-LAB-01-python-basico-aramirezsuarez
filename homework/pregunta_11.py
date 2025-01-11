def pregunta_11():
    """
    Retorne un diccionario que contenga la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabéticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
    """
    file_path = "./files/input/data.csv"
    try:
        # Abrimos y leemos el archivo
        with open(file_path, "r", encoding="utf-8") as file:
            data = file.readlines()

        # Crear un diccionario para almacenar las sumas
        letter_sums = {}

        # Procesar cada línea
        for line in data:
            try:
                # Separar las columnas
                columns = line.strip().split("\t")
                col2_value = int(columns[1])  # Columna 2 (valor numérico)
                col4_letters = columns[3].split(",")  # Columna 4 (lista de letras)

                # Sumar el valor de la columna 2 a cada letra de la columna 4
                for letter in col4_letters:
                    if letter in letter_sums:
                        letter_sums[letter] += col2_value
                    else:
                        letter_sums[letter] = col2_value
            except (IndexError, ValueError) as e:
                print(f"Error procesando línea: {line.strip()}. Detalle: {e}")
                continue

        # Ordenar el diccionario por clave (alfabéticamente)
        result = dict(sorted(letter_sums.items()))

        return result

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {file_path}")
        return {}

    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
        return {}

