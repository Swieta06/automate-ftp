# main.py

import logging
from file_handler import process_files
from config import FTP_PATHS
from ftp_util import upload_log_file


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )


if __name__ == '__main__':
    setup_logging()
    logging.info("=== Memulai proses otomatisasi Excel dari FTP ===")
    process_files()
    logging.info("=== Proses selesai ===")
