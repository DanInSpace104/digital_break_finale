from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Создается объект сообщения

# Данные авторизации


def send_email(to, title, content):
    message_object = MIMEMultipart()
    message_object['From'] = 'rossetiemail@gmail.com'
    password = 'Poiu0987'

    message_object['To'] = to
    message_object['Subject'] = title
    message_text = content

    # Добавляем тело сообщения
    message_object.attach(MIMEText(message_text, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()

    server.login(message_object['From'], password)
    server.sendmail(message_object['From'], message_object['To'], message_object.as_string())
    server.quit()

    print("Successfully sent email to %s:" % (message_object['To']))
