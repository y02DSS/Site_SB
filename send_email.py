from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
 
def send_for_email(text):
    msg = MIMEMultipart()
    
    password = "kabinet35"
    msg['From'] = "sbz35@mail.ru"
    msg['To'] = "sb-mail@bk.ru"
    msg['Subject'] = f'Позвонить!'

    msg.attach(MIMEText(text))

    server = smtplib.SMTP('smtp.mail.ru: 587')
    server.starttls()
    server.login(msg['From'], password)
    server.send_message(msg)
    server.quit()

    
