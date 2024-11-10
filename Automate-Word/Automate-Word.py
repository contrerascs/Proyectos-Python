from docxtpl import DocxTemplate
from datetime import datetime
import pandas as pd

mi_numero = '498-113-3003'
mi_correo = 'sam.contreras@gmail.com'
mi_direccion = '#13 Cornelia Street, NY'
date_today = datetime.today().strftime('%d %b, %Y')

#Creamos diccionario con datos estaticos
doc = DocxTemplate(r'Automate-Word\sp-plantilla-rrhh-info.docx')
my_context = {'mi_nombre': 'Sam Contreras', 'mi_numero': mi_numero,
           'mi_correo': mi_correo, 'mi_direccion': mi_direccion, 'fecha_hoy': date_today}

#Creamos diccionario con datos dinamicos
df = pd.read_csv(r'Automate-Word/test_data.csv')
for index, fila in df.iterrows():
    context = {
        'nombre_persona_rrhh' : fila['name'],
        'correo': fila['email'],
        'direccion': fila['address'],
        'puesto_trabajo': fila['job'],
        'nombre_empresa': fila['company'],
        'numero_telefono': fila['phone_number'],
    }

    context.update(my_context)
    doc.render(context)
    doc.save(rf'Automate-Word/Genereted_Docs/generated_doc_{index}.docx')