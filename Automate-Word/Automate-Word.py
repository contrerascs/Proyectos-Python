from docxtpl import DocxTemplate

doc = DocxTemplate(r'Automate-Word/sp-plantilla-mi-info.docx')
context = {'mi_nombre': 'Sam Contreras'}
doc.render(context)
doc.save(r'Automate-Word/generated_doc.docx')