import time
import sqlite3
from large_files import files

#La segunda parte consta de exportar los datos a SQLite para generar un reporte en consola 
#El reporta tambien se va a escribir en un archivo txt
inicio = time.time()

#Creamos la conección y el cursos para trabajar con él 
conn = sqlite3.connect(":memory:")
#conn =sqlite3.connect("reporte.sqlite")

    #** En este caso, se usa :memory: para no generar un archivo externo
cursor = conn.cursor()

#Se crea la tabla
cursor.execute(""" CREATE TABLE IF NOT EXISTS report 
                (id INTEGER PRIMARY KEY,
               path TEXT, size_Kb INTEGER)        
""")
# A continuación se utiliza como insumo para llenar la tabla la información del archivo creado
# large_files.yp
cursor.executemany(""" INSERT INTO report (path,size_Kb) VALUES (?,?)""",files)
    #** en lugar de usar un for con .execute() se opto por usar .executemany()

#CREACIÓN DEL REPORTE
with open("reporte.txt","w",encoding="utf-8") as reporte:
# Se crea el archivo reporte .txt donde se va a exportar toda la información
# Ya con la tabla creada, se puede proceder a realizar las busquedas que considere necesarias
    
    #Se reporta la cantidad de archivos totales
    cursor.execute("SELECT COUNT(id) from report")
    count = cursor.fetchone()
    print(f"El numero de rutas de archivo encontrados en large_files.py es de: {count[0]}")
    reporte.write(f"El numero de rutas de archivo encontrados en large_files.py es de: {count[0]}\n")
    
    # Se reporta la cantidad de archivos vacios
    cursor.execute("SELECT COUNT(id) from report WHERE size_Kb = 0")
    count = cursor.fetchone()
    print(f"Cantidad de arhivos con peso de 0Kb: {count[0]}")
    reporte.write(f"Cantidad de arhivos con peso de 0Kb: {count[0]}\n")
    
    # Se reporta la cantidad de archivos que son pesados (mayor a 2Kb)
    cursor.execute("SELECT COUNT(id) from report WHERE size_Kb > 2")
    count = cursor.fetchone()
    print(f"Cantidad de arhivos con peso mayor a 2Kb: {count[0]}\n")
    reporte.write(f"Cantidad de arhivos con peso mayor a 2Kb: {count[0]}\n")

    # Se pregunta por el numero de filas en el reporte
    # Se deja como opcion si se quiere quiere preguntar al usuario
    # por default se toman diez archivos
    #num = input("Numero de filas que quiere en el reporte: ")
    num = 10
    

    # Se hace un SELECT para buscar los 10 archivos mas pesados 
    lista_query = f"SELECT * from report ORDER BY size_Kb DESC LIMIT({num})"
    print("\n## Rutas con archivos mas pesados:")
    reporte.write("\n## Rutas con archivos mas pesados:\n")
    for i in cursor.execute(lista_query):
        print(f"Ruta: {i[1]}, \nTamaño: {i[2]}Kb")
        reporte.write(f"Tamaño: {i[2]}Kb, Ruta: {i[1]}\n")

    # Se hace un SELECT para buscar las primeras 10 lineas que sean archivos python
    filespy_query = f"SELECT * from report WHERE path lIKE'%.py' LIMIT({num})"
    print("\n##Rutas con extención '.py'")
    reporte.write("\n##Rutas con extención '.py'\n")
    for i in cursor.execute(filespy_query):
        print(f"Ruta: {i[1]}, \nTamaño: {i[2]}Kb")
        reporte.write(f"Ruta: {i[1]}, Tamaño: {i[2]}Kb\n")

    # Se hace un SELECT para buscar los archivos menos pesados que 1Kb 
    filespy_query = f"SELECT * from report WHERE size_Kb < 1 ORDER BY size_Kb DESC LIMIT({num})"
    print("\n##Rutas con archivos menores a 1Kb")
    reporte.write("\n##Rutas con archivos menores a 1Kb\n")
    for i in cursor.execute(filespy_query):
        print(f"Ruta: {i[1]}, \nTamaño: {i[2]:.3f}Kb")
        reporte.write(f"Tamaño: {i[2]:.3f}Kb, Ruta: {i[1]}\n")

    final = time.time() - inicio
    reporte.write(f"\nEl tiempo de ejecución del reporte fue de {final:.3f} seg ")
conn.commit()
conn.close()
print("Reporte guardado en 'Reporte.txt'")
