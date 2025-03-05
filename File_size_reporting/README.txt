File Size Reporting

DESCRIPCIÓN
Este proyecto es un script en Python que permite recorrer un directorio especifico y 
registrar en un archivo large_files.py todas las rutas de los archivos encontrados 
junto con sus tamanos en KB. Se puede proporcionar la ruta como argumento en la terminal
o usar una ruta por defecto (i.e. "C:\Users\LENOVO\OneDrive")

CARACTERISTICAS
- Usa os.walk para recorrer recursivamente todos los archivos de un directorio dado.
- Convierte las rutas en absolutas para evitar problemas de formato.
- Guarda los archivos en una lista antes de escribir en large_files.py, optimizando la escritura.
- Filtra archivos con errores de acceso o permisos.
- Limita la cantidad de archivos procesados a 2000 para evitar sobrecarga.
- Mide el tiempo de ejecucion del script.

INSTALACION
Clonar el repositorio
Comando en terminal para clonar el repositorio desde GitHub y acceder a la carpeta:
    $ git clone https://github.com/Leoperez9715/mis_proyectos.git
    $ git cd File_size_reporting

INSTALAR PYTHON SI NO LO TIENES
Este script requiere Python 3.6 o superior. Para verificar la version instalada, ejecuta:
    $ python --version

Si no tienes Python, puedes descargarlo desde la pagina oficial en python.org.

EJECUTAR EL SCRIPT
Para usar el script con una ruta personalizada, se debe ejecutar el siguiente comando en la terminal:
    $ python File_report_size.py "ruta" ejemplo: "C:\Users\LENOVO\Documents"
    #** La ruta debe estar entre comillas para ingresarlo como string

Si no se proporciona una ruta, el script usara la ruta por defecto C:\Users\LENOVO\OneDrive:
    $ python File_report_size.py

DEPENDENCIAS
El script usa solo librerias estandar de Python:
- os: Para gestionar rutas y recorrer directorios.
- argparse: Para manejar argumentos de la linea de comandos.
- time: Para medir el tiempo de ejecucion.

No se requieren instalaciones adicionales.

EXPLICACIÓN DEL CODIGO
1. Recorre el directorio con os.walk(path), obteniendo archivos y carpetas.
2. Convierte las rutas a formato absoluto usando os.path.abspath().
3. Filtra archivos con errores de acceso como FileNotFoundError y PermissionError.
4. Guarda la informacion en large_files.py en formato de lista de tuplas con la ruta y 
5. Usa argparse para permitir que el usuario defina la ruta de busqueda desde la terminal.

HABILIDADES DE DATA SCIENCE EMPLEADAS
- Manejo de archivos y directorios: Uso de os.walk y os.path para recorrer y procesar archivos.
- Optimizacion de procesos: Uso de listas para acumular datos antes de escribir en un archivo.
- Automatizacion con scripts CLI: Uso de argparse para permitir ejecucion flexible desde la terminal.
- Manejo de excepciones: Evita que errores de acceso interrumpan la ejecucion.
- Medicion de tiempos de ejecucion: Con time.time() para evaluar eficiencia.

## Contacto 🤝
Si tienes preguntas o sugerencias, no dudes en contactarme:
📧 Email: leoperez9715@gmail.com 
🐍 GitHub: [@Leoperez9715](https://github.com/Leoperez9715)

