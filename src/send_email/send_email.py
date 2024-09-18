import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()


SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587  
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD_EMAIL')
FROM_EMAIL = os.getenv('FROM_EMAIL')
TO_EMAIL = os.getenv('TO_EMAIL')
SUBJECT = os.getenv('SUBJECT')

def send_message_email(body: str):
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = TO_EMAIL
    msg['Subject'] = SUBJECT
    msg.attach(MIMEText(body, 'plain'))
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  
        server.login(USERNAME, PASSWORD)  
        server.send_message(msg)  
        print('Письмо успешно отправлено!')
    except Exception as e:
        print(f'Произошла ошибка: {e}')
    finally:
        server.quit()  