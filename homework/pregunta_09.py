def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}
    """
    file_path = './files/input/data.csv'
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            data = f.readlines()

        result = {}

        columna = [line.strip().split()[4].split(',') for line in data]

        for c in columna:
            for i in c:
                try:
                    key = i.split(':')[0]
                    if key not in result:
                        result[key] = 1
                    else:
                        result[key] += 1
                except IndexError as e:
                    print(f"Error al procesar el elemento '{i}': {e}")
                    continue

        result = dict(sorted(result.items()))
        return result

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {file_path}")
        return {}

    except Exception as e:
        print(f"Se produjo un error: {e}")
        return {}


