def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    file_path = './files/input/data.csv'
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            data = f.readlines()

            meses = {line.split()[2].split('-')[1]: 0 for line in data}

            list(map(lambda line: meses.update({line.split()[2].split('-')[1]: meses[line.split()[2].split('-')[1]] + 1}), data))

            return sorted(meses.items())

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {file_path}")
        return []

    except Exception as e:
        print(f"Se produjo un error: {e}")
        return []
    
