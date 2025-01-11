def pregunta_12():
    """
    Genere un diccionario que contenga como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}
    """
    file_path = "./files/input/data.csv"
    try:
        # Abrir y leer el archivo
        with open(file_path, "r", encoding="utf-8") as file:
            data = file.readlines()

        # Diccionario para almacenar los resultados
        result = {}

        # Procesar cada línea
        for line in data:
            try:
                # Separar las columnas
                columns = line.strip().split("\t")
                col1 = columns[0]  # Columna 1 (letra)
                col5_items = columns[4].split(",")  # Columna 5 (lista de pares clave:valor)

                # Sumar los valores numéricos de la columna 5
                col5_sum = sum(int(item.split(":")[1]) for item in col5_items)

                # Actualizar el diccionario con la suma
                if col1 in result:
                    result[col1] += col5_sum
                else:
                    result[col1] = col5_sum

            except (IndexError, ValueError) as e:
                print(f"Error procesando línea: {line.strip()}. Detalle: {e}")
                continue

        return result

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {file_path}")
        return {}

    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
        return {}

