import smtplib
from email.message import EmailMessage
from config import EMAIL_CONFIG


def send_email_invalid_file(file_name):
    msg = EmailMessage()
    msg['Subject'] = 'File Excel Tidak Valid'
    msg['From'] = EMAIL_CONFIG['sender_email']
    msg['To'] = EMAIL_CONFIG['receiver_email']
    msg.set_content(
        f"File '{file_name}' tidak sesuai format penamaan yang disepakati (laporanDDMMYYYY.xlsx). Harap diperbaiki."
    )

    with smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port']) as server:
        server.starttls()
        server.login(EMAIL_CONFIG['sender_email'], EMAIL_CONFIG['sender_password'])
        server.send_message(msg)
