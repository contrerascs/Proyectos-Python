from Credenciales import EMAIL, RECEPTOR, PASSWORD
from email.message import EmailMessage
import ssl 
import smtplib

email_emisor = EMAIL
email_contraseña = PASSWORD
email_receptor = RECEPTOR

asunto = 'Revisa mi blog en Instagram'
cuerpo = '''
Mira el nuevo video de Mr Irrelevant: https://www.instagram.com/reel/DCgNqmfobxg/
'''

em = EmailMessage()
em['From'] = email_emisor
em['To'] = email_receptor
em['Subject'] = asunto
em.set_content(cuerpo)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_emisor, email_contraseña)
    smtp.sendmail(email_emisor, email_receptor,em.as_string())