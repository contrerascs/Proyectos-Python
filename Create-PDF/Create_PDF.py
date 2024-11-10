import pdfkit
import jinja2
from datetime import datetime

my_name = 'Sam Contreras'
COY = 'Dan Campbell'
CPOY = 'Kirk Cousins'
DROY = 'Jared Verse'
OROY = 'Jayden Daniels'
DPOY = 'T.J. Watt'
OPOY = 'Derrick Henry'
MVP = 'Jared Goff'
today_date = datetime.today().strftime("%d %b, %Y")

context = {'COY': COY, 'CPOY': CPOY, 'DROY': DROY, 'OROY': OROY,
           'DPOY': DPOY, 'OPOY': OPOY, 'MVP': MVP, 'my_name': my_name ,'today_date': today_date}

template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

html_template = 'Plantilla.html'
template = template_env.get_template(html_template)
output_text = template.render(context)

config = pdfkit.configuration(wkhtmltopdf = r'D:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
output_pdf = 'pdf_generado.pdf'

pdfkit.from_string(output_text, output_pdf, configuration=config, css='style.css')