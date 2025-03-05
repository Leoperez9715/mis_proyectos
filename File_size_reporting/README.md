
# Repositorio de Análisis de Archivos
Este repositorio contiene scripts para analizar archivos en un directorio, extraer información relevante y generar reportes en diferentes formatos.

## Contenido del Repositorio
### 1. large_files.py
Este script escanea un directorio especificado y genera una lista de archivos con sus respectivas rutas y tamaños en kilobytes.

- Utiliza os.walk() para recorrer los archivos.
- Almacena los resultados en una lista de tuplas.
- Genera un archivo large_files.py que contiene estos datos estructurados.

### Ejecutar el script
Para usar el script con una ruta personalizada, se debe ejecutar el siguiente comando en la terminal:
$ python File_report_size.py "ruta" (ejemplo: "C:\Users\LENOVO\Documents")
*_Nota_*: La ruta debe estar entre comillas para ingresarlo como string
Si no se proporciona una ruta, el script usara la ruta por defecto C:\Users\LENOVO\OneDrive:
*_Nota_*: La ruta default se puede cambiar en ´add.arguments(default="nueva_ruta")´
$ python File_report_size.py

### 2. report_SQL.py
- Este script carga los datos del archivo large_files.py en una base de datos SQLite en memoria y genera reportes en consola y en un archivo de texto reporte.txt.
- Crea una base de datos SQLite en memoria.
- Inserta los datos extraídos en una tabla llamada report.
- Genera métricas sobre los archivos, como:
    - Número total de archivos.
    - Cantidad de archivos vacíos (0 KB).
    - Cantidad de archivos grandes (> 2 KB).

- Extrae listas de archivos según criterios específicos:
- Archivos más pesados.
- Archivos con extensión .py.
- Archivos con tamaño menor a 1 KB.
- Guarda todos estos reportes en reporte.txt.

## HABILIDADES DE DATA SCIENCE EMPLEADAS
- Manejo de archivos y directorios: Uso de os.walk y os.path para recorrer y procesar archivos.
- Optimizacion de procesos: Uso de listas para acumular datos antes de escribir en un archivo.
- Automatizacion con scripts CLI: Uso de argparse para permitir ejecucion flexible desde la terminal.
- Manejo de excepciones: Evita que errores de acceso interrumpan la ejecucion.
- Medicion de tiempos de ejecucion: Con time.time() para evaluar eficiencia.
- Automatización: Extracción y almacenamiento automatizado de información sobre archivos.
- Manejo de bases de datos: Uso de SQLite para almacenar y consultar datos.
- Generación de reportes: Creación de archivos estructurados con información clave.
- Optimización de scripts: Uso de executemany() para insertar múltiples registros de manera eficiente.

## Caracteristicas
- Usa os.walk para recorrer recursivamente todos los archivos de un directorio dado.
- Convierte las rutas en absolutas para evitar problemas de formato.
- Guarda los archivos en una lista antes de escribir en large_files.py, optimizando la escritura.
- Filtra archivos con errores de acceso o permisos.
- Limita la cantidad de archivos procesados a 2000 para evitar sobrecarga.
- Mide el tiempo de ejecucion del script.

## INSTALACION
Clonar el repositorio
Comando en terminal para clonar el repositorio desde GitHub y acceder a la carpeta:
$ git clone https://github.com/Leoperez9715/mis_proyectos.git
$ git cd File_size_reporting

## INSTALAR PYTHON SI NO LO TIENES
Este script requiere Python 3.6 o superior. Para verificar la version instalada, ejecuta:
$ python --version

## Librerías Utilizadas
* *os:* Para recorrer directorios y obtener información de archivos.
* *argparse:* Para permitir la entrada de rutas personalizadas desde la terminal.
* *sqlite3:* Para almacenar los datos en una base de datos y realizar consultas.
* *time:* Para medir el tiempo de ejecución del script.
No se requieren instalaciones adicionales.

## Contacto 🤝
Si tienes preguntas o sugerencias, no dudes en contactarme:
📧 Email: leoperez9715@gmail.com 
🐍 GitHub: [@Leoperez9715](https://github.com/Leoperez9715)

