import os
import argparse
import time

# Se marca el inicio del proceso
inicio = time.time()

# Se define la función que va a guardar las rutas y los tamaños de archivos en un archivo .py
def add_to_file(path):
    print(path)
    ruta = ruta = os.path.abspath(path)
    print(ruta)
    #** Se usa .abspath() para convertir la entrada en ruta absoluta sin modificarla 
    #** esta es una función que se encarga de arreglar el formato para walk en lugar de yo modificar el codigo.
    
    # Inicializo el contador de archivos y la lista donde voy a guardar los tuples antes de escribir el .py
    counter = 0
    archivos = []  # Lista para almacenar archivos antes de escribir

    #Primer for donde voy a hacer el walk desde la ruta dada 
    for root, directories, files in os.walk(ruta):
        #Segundo for donde voy a trabajar con los archivos puntuales encontrados y crear rutas
        for _file in files:
            if counter >= 2000:  # Evitar escribir más de 2000 archivos
                break
            try: 
                absolute_path = os.path.abspath(os.path.join(root, _file))
                #** con join(root,_file) creo la ruta desde root hasta el archivo
                #** abspath() asegura que el formato siempre sera el correcto para trabajarlo
                file_size = os.path.getsize(absolute_path) / 1000  # Convertir bytes a KB

                #A continuación se hace una validación, que la ruta inicie con el argumento dado
                if not absolute_path.startswith(ruta):
                    absolute_path = os.path.join(ruta, _file)
                    # Se vuelve a revisar en caso de que haya error de codificación de las rutas
            
                #Cuando ya se paso por los filtros, se procede a agregar a la lista
                archivos.append(f"({repr(absolute_path)}, {file_size})")
                #** Al momento de escribir en el .py se escribe como un tuple
                counter += 1 
                # Se suma 1 al counter 
            except (FileNotFoundError, PermissionError):
                continue

    # Si hay archivos, escribirlos correctamente
    # Una vez se almacena toda la info en una lista, se procede a crear el archivo .py 
    # Cada linea sera un tuple con la información de (ruta, size)
    if archivos:
        with open("./large_files.py", "w", encoding="utf-8") as _files:
            #** ./ indica que quiero guardar el archivo en la carpeta actual
            _files.write("files = [\n")
            _files.write(",\n".join(archivos))  # Escribir correctamente cada línea
            _files.write("\n]")  # Cerrar la lista

#Ahora se va a usar un CLI cob argparse para poder ingresar la ruta desde la terminal como un argumento
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?",
                         default="C:\\Users\\LENOVO\\OneDrive", 
                        help="Ruta desde donde se van a buscar archivos, entre comillas (""); \n valor por defecto 'C:\\Users'")
    argumentos = parser.parse_args()
    add_to_file(argumentos.path)

if __name__ == "__main__":
    main()

#Medicion del tiempo para ver cuanto se demora el script hasta el momento. 
final_primera_parte = time.time() - inicio
print(final_primera_parte)

