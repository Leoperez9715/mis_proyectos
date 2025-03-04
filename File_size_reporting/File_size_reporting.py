#Recolectar datos del directorios
import os
import argparse

#Ingreso de la ruta, por el momento se da la ruta, mas adelante se agrega el argparse
ruta = (r"c:\Users\LENOVO\OneDrive\src")

def add_to_file (ruta):
    #Revisar los documentos de una ruta establecida
    counter = 0
    with open("./large_files.py","w", encoding="utf-8") as _files:
        #** Cree el archivo large_files.py si ya existe, lo sobreescribe
        _files.write("files = [\n")
        #** inicio el archivo, escribiendo el inicio de una lista que voy a ir llenando con los files

        #Ahora, inicio a extraer la información e los archivos y sus rutas   
        with open("./large_files.py","a", encoding="utf-8") as _files:
            #Se hace un for para extraer los archivos
            for root, directories, files in os.walk(ruta):
                for _file in files:
                    # Uso un counter para que el sistema no se sature, solo obteber 2000 archivos
                    if counter > 2000:
                        break
                    try: 
                        absolute_path = os.path.join(root,_file)
                        #** Obteno la ruta de cada archivo uniendo la ruta hasta la carpeta y nombre
                        file_size = (os.path.getsize(absolute_path))/1000
                        #** Obtengo el tamaño el archico en bytes y lo divido en mil para kb
                    except (FileNotFoundError,PermissionError):
                        continue
                        #En este momento se almacena en un directorio en cada k:v el path:tamaño(Kb)
                    _files.write(f"('{absolute_path}',{file_size}),\n")
                    #** Sobreescribo el archivo _files (large_files.py) un tuplas
                    #** cada tupla tiene ("path"(str), size(int)) y un salto de linea
                    counter +=1
            _files.write("]")
            #** Con esto cierro la lista que he estado sobreescribiendo. 

