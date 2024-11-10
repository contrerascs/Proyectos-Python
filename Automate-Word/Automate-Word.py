from docxtpl import DocxTemplate
from datetime import datetime

mi_numero = '498-113-3003'
mi_correo = 'sam.contreras@gmail.com'
mi_direccion = '#13 Cornelia Street, NY'
date_today = datetime.today().strftime('%d %b, %Y')

doc = DocxTemplate(r'Automate-Word/sp-plantilla-mi-info.docx')
context = {'mi_nombre': 'Sam Contreras', 'mi_numero': mi_numero,
           'mi_correo': mi_correo, 'mi_direccion': mi_direccion, 'fecha_hoy': date_today}
doc.render(context)
doc.save(r'Automate-Word/generated_doc.docx')