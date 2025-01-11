def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado más
    pequeño y el valor asociado más grande computados sobre todo el archivo.

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
    file_path = './files/input/data.csv'
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            data = f.readlines()

            lineas = [line.split()[4].split(',') for line in data]
            result = {}

            for line in lineas:
                for item in line:
                    try:
                        clave, valor = item.split(':')
                        valor = int(valor)
                        if clave not in result:
                            result[clave] = [valor, valor]
                        else:
                            result[clave][0] = min(result[clave][0], valor)
                            result[clave][1] = max(result[clave][1], valor)
                    except ValueError as ve:
                        print(f"Error al procesar el par clave:valor '{item}': {ve}")
                        continue

            return sorted((clave, valores[0], valores[1]) for clave, valores in result.items())

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {file_path}")
        return []

    except Exception as e:
        print(f"Se produjo un error: {e}")
        return []
