import sqlite3

def main():
    crearTabla()

    insert('Fabricio', 'Navarro')
    insert('Matías', 'Pérez')
    insert('Sebastian', 'Toledo')
    insert('Agustín', 'Rodríguez')
    insert('Sofía', 'López')
    insert('Andrés', 'Cortés')
    insert('Lucía', 'Qwerty')
    insert('Marta', 'Uiop')

    busqueda('Mariana')
    busqueda('Sofía')

def crearTabla():
    """Crear el archivo .db y la tabla"""
    conn = sqlite3.connect("ejercicio_tema_11.db")
    cursor = conn.cursor()
    # Creación de la tabla Alumnos
    query = "CREATE TABLE Alumnos(id INT, nombre TEXT, apellido TEXT);"
    cursor.execute(query)
    cursor.close()
    conn.close()

# id para aumentar automaticamente el id 
# cada vez que se llama a la función insert()
id = 0
def insert(nombre, ape):
    """ Crea elementos en la tabla Alumnos"""
    global id
    id += 1
    conn = sqlite3.connect("ejercicio_tema_11.db")
    cursor = conn.cursor()
    query = f"INSERT INTO Alumnos (id, nombre, apellido) VALUES ({id}, '{nombre}', '{ape}');"
    cursor.execute(query)

    # Confirmando cambios
    conn.commit()

    cursor.close()
    conn.close()

def busqueda(nombre):
    """ Devuelve información del alumno, si existen alumnos con ese 
    nombre en la tabla """
    conn = sqlite3.connect("ejercicio_tema_11.db")
    cursor = conn.cursor()
    # Seleccionamos toda la información disponible en la tabla Alumnos
    # solo si hay coincidencias
    query = f"SELECT * FROM Alumnos WHERE nombre = '{nombre}';"
    rows = cursor.execute(query)
    # Mostrando resultados de busqueda por consola
    data = rows.fetchone()
    print(f"Se obtuvieron resultados: \n{data}") if data else print(f"No se encontraron coincidencias para: {nombre}")

    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()
