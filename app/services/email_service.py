import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email_validator import validate_email, EmailNotValidError
from fastapi import HTTPException
from app.core.config import get_settings


SMTP_SERVER = get_settings().smtp_server
SMTP_PORT = get_settings().smtp_port
SENDER_EMAIL = get_settings().sender_email
SENDER_PASSWORD = get_settings().sender_password

# Función para enviar un correo electrónico
def send_email(recipient_email: str, subject: str, body: str):
    try:
        validate_email(recipient_email)
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, recipient_email, msg.as_string())

        return True
    except EmailNotValidError:
        raise HTTPException(status_code=400, detail="Correo no válido")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error enviando correo: {e}")