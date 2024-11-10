import pdfkit
import jinja2
from datetime import datetime

store_name = 'Midnights Store'
direction = 'Cornelia Street #13'
my_name = 'Sam Contreras'
item1 = 'Super Smash Bros Ultimate'
description1 = 'Video Game Fight'
item2 = 'Madden 24'
description2 = 'Sport video game'
item3 = 'Zelda: Breath Of The Wild'
description3 = 'Open-world adventure game for Nintendo Switch'
today_date = datetime.today().strftime("%d %b, %Y")

subttotal1 = 399
subttotal2 = 449
subttotal3 = 559

context = {'item1': item1, 'description1': description1, 'subtotal1': f'${subttotal1}', 
           'item2': item2, 'description2': description2, 'subtotal2': f'${subttotal2}', 
           'item3': item3, 'description3': description3, 'subtotal3': f'${subttotal3}',
           'my_name': my_name ,'date': today_date,
           'store_name': store_name, 'direction': direction}

template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

html_template = 'Plantilla2.html'
template = template_env.get_template(html_template)
output_text = template.render(context)

config = pdfkit.configuration(wkhtmltopdf = r'D:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
output_pdf = 'pdf_avanzado.pdf'

pdfkit.from_string(output_text, output_pdf, configuration=config, css='style.css')