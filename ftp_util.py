from ftplib import FTP, error_perm
from io import BytesIO
import logging
from config import FTP_CONFIG, FTP_PATHS


def connect_ftp():
    ftp = FTP()
    ftp.connect(FTP_CONFIG['host'], FTP_CONFIG['port'])
    ftp.login(FTP_CONFIG['user'], FTP_CONFIG['passwd'])
    return ftp


def list_files(path):
    with connect_ftp() as ftp:
        ftp.cwd(path)
        return ftp.nlst()


def download_file(path, filename):
    with connect_ftp() as ftp:
        ftp.cwd(path)
        bio = BytesIO()
        ftp.retrbinary(f'RETR {filename}', bio.write)
        bio.seek(0)
        return bio


def move_file(filename, src_path, dest_path):
    with connect_ftp() as ftp:
        ftp.cwd(src_path)
        temp = BytesIO()
        ftp.retrbinary(f'RETR {filename}', temp.write)
        temp.seek(0)

        ftp.cwd(dest_path)
        ftp.storbinary(f'STOR {filename}', temp)

        ftp.cwd(src_path)
        ftp.delete(filename)


def upload_log_file(log_content: str, filename: str = "process.log"):
    with connect_ftp() as ftp:
        ftp.cwd(FTP_PATHS['logs'])
        content = BytesIO(log_content.encode('utf-8'))
        ftp.storbinary(f'STOR {filename}', content)
