import pandas as pd
import time

#Se le pregunta al usuario la inicial o nombre del pokemón
#Se hace un try-except para que se ingrese la información correcta
# while True: 
#     try:
#         letter = str.upper(input("inicial o nombre del pokemon: "))
#         print(type(letter))
#         if len(letter) > 0:
#             break
#         else:
#             print("Debe ingresar algun dato")
#     except:
#         print("Debe ingresar un nombre valido")
letter = str.upper("a")
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
    columna = lista_columnas[num-1]
    #print(columna)
    return columna

def stats_totales(row):
    name = row["Pokemon"]
    print(name)
    HP = row[["HP Min","HP Base","HP Max"]]
    #print(HP)
    Attack = row[["Attack Min","Attack Base","Attack Max"]]
    #print(Attack)
    Defense = row[["Defense Min","Defense Base","Defense Max"]]
    #print(Defense)
    S_Attack = row[["Special Attack Min","Special Attack Base","Special Attack Max"]]
    #print(S_Attack)
    S_Defense = row[["Special Defense Min","Special Defense Base","Special Defense Max"]]
    #print(S_Defense)
    Velocity = row[["Speed Min","Speed Base","Speed Max"]]
    #print(Velocity)

    Totales = []
    for i in range(len(HP)):
        Totales.append(HP.iloc[i] + Attack.iloc[i] + Defense.iloc[i] + S_Attack.iloc[i] + S_Defense.iloc[i] + Velocity.iloc[i])
    #print(Totales, type(Totales))
    
    return  Totales

obt_info(num)
#Se aplica un filtro para buscar en el DF
df_filtered = Data[Data["Pokemon"].str.contains(f"^{letter}",case=False,regex=True)].reset_index()
df_filtered[["Stat_Min","Stat_Base","Stat_Max"]] = df_filtered.apply(stats_totales,axis=1).tolist()

#df_filtered = df_filtered.sort_values(by="Total Stats Base",ascending=False).reset_index()

print(df_filtered.loc[0:10,["Pokemon",f"{obt_info(num)}","Stat_Min","Stat_Base","Stat_Max"]])


