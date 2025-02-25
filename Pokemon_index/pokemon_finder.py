import pandas as pd

#Se le pregunta al usuario la inicial o nombre del pokemón
while True: 
    try:
        letter = str.upper(input("inicial o nombre del pokemon: "))
        print(type(letter))
        if len(letter) > 0:
            break
        else:
            print("Debe ingresar algun dato")
    except:
        print("Debe ingresar un nombre valido")


#letter = str.upper("ab")
    #** La letra no nombre se pasa siempre a mayuscula para evitar errores de escritura

#Se carga la base de datos para comenzar a trabajar con ellos
Data = pd.read_csv("pokemonDB_dataset.csv")

# se guardan las columnas en una lista para ser usadas mas tarde en otra función
cont = 1
lista_columnas = []
for columna in Data.columns:
    lista_columnas.append(columna)
    #** se muestran las columnas con indices para que el usuario elija la información que quiere conocer    
    print (str(cont) + " " + str(columna))
    cont += 1

# Se solicita al usuario que de un numero de alguna de las columnas para poder entregarle esa información mas adelante. 
while True:
    try:
        num = int(input("¿qué información quieres saber? \nIngresa un número entre 1 y 32: "))
        
        # Validar si está dentro del rango permitido
        if 1 <= num <= 32:
            #print(f"✅ Número válido: {num}")
            break  # Salir del loop si la entrada es correcta
        else:
            print("❌ Error: El número debe estar entre 1 y 32.")
    
    except ValueError:
        print("❌ Error: Debes ingresar un número válido.")


#Se aplica un filtro para buscar en el DF
df_filtered = Data[Data["Pokemon"].str.contains(f"^{letter}",case=False,regex=True)].reset_index()
    #** se busca que se ignore si es mayus/minus y que el nombre inicie con la letra 
print(df_filtered[["Pokemon","Type"]])

