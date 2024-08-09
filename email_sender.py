# email_sender.py

import smtplib
import ssl
from config import SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD

def send_email(target_email, subject, body):
    context = ssl.create_default_context()
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls(context=context)
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(SENDER_EMAIL, target_email, message)
