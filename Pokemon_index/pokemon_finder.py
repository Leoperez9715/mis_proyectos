import pandas as pd
import time

#Se le pregunta al usuario la inicial o nombre del pokemón
#Se hace un try-except para que se ingrese la información correcta
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
#letter = str.upper("a")
    #** La letra no nombre se pasa siempre a mayuscula para evitar errores de escritura
print("...")
time.sleep(1)

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
# Se realiza un try-Except para validar que el usuario entregue un valor valido
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

def obt_info (num): 
    #Con el valor dado del usuario, se usa la función para entregar el nombre de dicha columna
    columna = lista_columnas[num-1]
    return columna

def stats_totales(row):
    #función para obtener los totales min, base, max de cada tipo de stat de una fila

    HP = row[["HP Min","HP Base","HP Max"]]
    Attack = row[["Attack Min","Attack Base","Attack Max"]]
    Defense = row[["Defense Min","Defense Base","Defense Max"]]
    S_Attack = row[["Special Attack Min","Special Attack Base","Special Attack Max"]]
    S_Defense = row[["Special Defense Min","Special Defense Base","Special Defense Max"]]
    Velocity = row[["Speed Min","Speed Base","Speed Max"]]

    #Se usa un for para obtener una lista con los totales de cada stat de cada row ingresada a la fun 
    Totales = []
    for i in range(len(HP)):
        Totales.append(HP.iloc[i] + Attack.iloc[i] + Defense.iloc[i] + S_Attack.iloc[i] + S_Defense.iloc[i] + Velocity.iloc[i])
    
    #La función retorna una lista [1x3] que se toma como un set. 
    return  Totales


#Se aplica un filtro para buscar en el DF
df_filtered = Data[Data["Pokemon"].str.contains(f"^{letter}",case=False,regex=True)].reset_index()
    #** Se usar REGEX para evitar problemas con mayus/minus
    #** Con la información de letras del usuario se crea una mask para filtrar la base de datos
    #** Se ajustan los indices de esta lista para que esten en orden

df_filtered[["Stat_Min","Stat_Base","Stat_Max"]] = df_filtered.apply(stats_totales,axis=1).tolist()
    #** se aplica la función de sum_totales para obtener 3 nuevas columnas 

#Se realiza un sort sobre la DF filtrada con la función aplicada de mayor a menor sobre stat_base 
#df_filtered = df_filtered.sort_values(by="Total Stats Base",ascending=False).reset_index()

#Se retorna el DF filtrado con el nombre de los pokemnos, la info solicitdad por el usuario 
# y un resumen de los totales maximos, minimos y base de todo
print(df_filtered.loc[0:10,["Pokemon",f"{obt_info(num)}","Stat_Min","Stat_Base","Stat_Max"]])


