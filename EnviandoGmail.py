import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Corpo do Email
msg = MIMEMultipart()
message = "Você recebeu E-mail através do Python =) "

# Informações de acesso e Assunto do E-mail

from config import email, passw

password = passw
msg['From'] = email
msg['To'] = "j.costa13@hotmail.com"
msg['Subject'] = "E-mail através do Python"

# Monta conexão e envia o e-mail
msg.attach(MIMEText(message, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', port=587)
server.starttls()
server.login(msg['From'], password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()