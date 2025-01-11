def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    file_path = './files/input/data.csv'
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            data = f.readlines()

            letras = [str(fila.split()[0]) for fila in data]
            set_letras = sorted(set(letras))

            conteo = [(letra, letras.count(letra)) for letra in set_letras]

            return conteo

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {file_path}")
        return []

    except Exception as e:
        print(f"Se produjo un error: {e}")
        return []

