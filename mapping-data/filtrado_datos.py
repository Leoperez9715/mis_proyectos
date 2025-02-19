from csv import DictReader
import pandas as pd

#USO DE CSV
with open('sample_data/wine-ratings-small.csv', encoding='utf-8', errors='ignore') as f:
    reader = DictReader(f)
    wines = list(reader)
    #lista de la forma [{k:v},{k:v}]
    #Es una lista de diccionarios
#print(type(reader))
#print(type(wines),len(wines))

#USO DE PANDAS 
df = pd.read_csv('sample_data/wine-ratings-small.csv')
#print(df["variety"])
    #** La información se importo correctamente

print(df.columns)
    #** Se obtiene los nombres de las columnas para trabajar en ellas

#Proceso de filtrado
print("las dimensiones de la tabla son: ", df.size)


#Filter = (df.loc[df["variety"] == "White Wine"]) & (df["rating"]>=90) &(df["rating"]<=92)
Filter = (df["rating"]>=90) & (df['rating']<= 92) & (df["variety"] == "Red Wine")
    # Filtro N°1: la calificación del vino debe estar entre 90 y 92 
    # Filtro N°2: el tipo de vino debe ser Red wine 

#Con el filtro, ahora se aplica al df para obtener el nuevo dataframe 
new_df = df[Filter]


print(Filter)
print(new_df.iloc[:20,0:6])
print("las dimensiones de la nueva tabla son: ", new_df.size)



#USO COMO DICCIONARIO 
#Enviar la tabla a diccionario
dict_data = df.to_dict()
#print(dict_data["variety"][0],dict_data["rating"][0],dict_data["region"][0])
