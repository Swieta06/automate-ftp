from datetime import datetime

# FTP configuration
FTP_CONFIG = {
    'host': 'localhost',  # atau IP dari FTP server
    'port': 21,
    'user': '',
    'passwd': ''
}

# Remote FTP folders
FTP_PATHS = {
    'data': '/datas/',
    'archive': '/archive/',
    'error': '/error/',
    'logs': '/logs/'
}

# File name expected today
TODAY_FILENAME = f"laporan{datetime.now().strftime('%d%m%Y')}.xlsx"

# Email configuration
EMAIL_CONFIG = {
    'smtp_server': 'smtp.office365.com',
    'smtp_port': 587,
    'sender_email': '',
    'sender_password': '',
    'receiver_email': ''
}

# SQL Server configuration
DB_CONFIG = {
    'driver': '{SQL Server}',
    'server': 'localhost',
    'database': '',
    'username': '',
    'password': ''
}
