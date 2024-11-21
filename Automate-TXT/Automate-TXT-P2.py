import pandas as pd

#Leer 1 CSV
df_numero_telefonos = pd.read_csv(r'Automate-TXT/numero-telefonos.csv', names=['numero-telefonos'])
#print(df_numero_telefonos)

#Creamos una nueva columna para comparar resultados
df_numero_telefonos['codigo-pais'] = df_numero_telefonos['numero-telefonos'].apply(lambda x: f'+52 {x}')
print(df_numero_telefonos)

#Leer Multiples CSV
nombres_archivos = ['numero-telefonos','numero-telefonos-2']

for archivo in nombres_archivos:
    df = pd.read_csv(rf'Automate-TXT/{archivo}.csv', names=['numero-telefonos'])
    df['codigo-pais'] = df['numero-telefonos'].apply(lambda x: f'+52 {x}')
    df.to_csv(rf'Automate-TXT/Archivos_Creados/codigo-{archivo}.csv', index=False)