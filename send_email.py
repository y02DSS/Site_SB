from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
 
def send_for_email(text):
    msg = MIMEMultipart()
    
    password = "qetGLzNTmCd49kpukyxz"
    msg['From'] = "sbz35@mail.ru"
    msg['To'] = "za02za02@bk.ru"
    msg['Subject'] = f'Позвонить!'

    msg.attach(MIMEText(text))

    server = smtplib.SMTP('smtp.mail.ru: 587')
    server.starttls()
    server.login(msg['From'], password)
    server.send_message(msg)
    server.quit()

    
