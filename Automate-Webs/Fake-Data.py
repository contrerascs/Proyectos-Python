import pandas as pd
from faker import Faker

#Creamos data falsa: nombre, email, direccion
fake = Faker()
profiles = [fake.profile() for i in range(10)]

#Acomodamos la data falsa en DataFrame
df = pd.DataFrame(profiles)
df = df[['name', 'mail', 'address']]

#creamos data falsa: numero de telefono, comentaios
numeros = [fake.phone_number() for i in range(0,10)]
comentario = '-'

#Acomodamos la data falsa en Pandas
df['Numero telefonico'] = numeros
df['Comentarios'] = comentario

#cambiar nombre de columnas
df.rename(columns={'name': 'Nombre', 'mail': 'Correo electronico', 'address': 'Direccion'}, inplace=True)

#exportar DataFrame a archivo csv
df.to_csv(r'Automate-Webs/fake_data.csv', index=False)