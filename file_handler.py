import pandas as pd
import logging
from config import TODAY_FILENAME, FTP_PATHS
from ftp_util import list_files, download_file, move_file, upload_log_file
from db import insert_to_db
from email_util import send_email_invalid_file


def process_files():
    logs = []
    files = list_files(FTP_PATHS['data'])

    for file in files:
        logs.append(f"Mendeteksi file: {file}")

        if file.strip().lower() == TODAY_FILENAME.lower():
            try:
                file_content = download_file(FTP_PATHS['data'], file)
                df = pd.read_excel(file_content)
                insert_to_db(df)
                move_file(file, FTP_PATHS['data'], FTP_PATHS['archive'])
                logs.append(f"Berhasil proses dan pindahkan file: {file}")
            except Exception as e:
                move_file(file, FTP_PATHS['data'], FTP_PATHS['error'])
                logs.append(f"Gagal proses file {file}: {str(e)}")
        else:
            send_email_invalid_file(file)
            move_file(file, FTP_PATHS['data'], FTP_PATHS['error'])
            logs.append(f"File tidak valid dipindahkan ke error: {file}")

    log_text = "\n".join(logs)
    logging.info(log_text)
    upload_log_file(log_text)
