# 📦 Project: excel\_ftp\_to\_sql\_v2

Sistem otomatisasi untuk:

* Mengambil file Excel dari server FTP
* Memvalidasi nama file sesuai format `laporanDDMMYYYY.xlsx`
* Memasukkan isi file ke database SQL Server
* Menangani error, mengirim email notifikasi, dan mencatat log

---

## 🗂️ Struktur Folder di FTP

```
/
├── datas/       # Folder tempat meletakkan file Excel dari user
├── archive/     # Folder arsip file yang berhasil diproses
├── error/       # Folder file gagal proses atau salah format
├── logs/        # Folder log proses
```

---

## ⚙️ Teknologi

* Python 3.9+
* pandas
* openpyxl
* pyodbc
* ftplib, smtplib (built-in)

---

## 📁 Struktur File Python

```
.
├── main.py
├── config.py
├── db.py
├── email_util.py
├── file_handler.py
├── ftp_util.py
├── requirements.txt
└── README.md
```

---

## ▶️ Cara Menjalankan

### 1. Setup .env

```bash
python setup_env.py
```

### 2. Install library

```bash
pip install -r requirements.txt
```

### 3. Konfigurasi

Edit `config.py`:

* `FTP_CONFIG` → isi host, user, pass FTP
* `DB_CONFIG` → koneksi ke SQL Server
* `EMAIL_CONFIG` → SMTP Outlook & penerima

### 4. Jalankan

```bash
python main.py
```

---

## 📌 Format File Excel

* **Nama file**: `laporanDDMMYYYY.xlsx`
* **Kolom wajib**: `id`, `nama`, `norek`, `cif`, `deskripsi`
* Hanya 1 file per hari yang valid

---

## ✅ Flow Proses

1. Ambil list file dari `/datas/` (FTP)
2. Cek apakah ada file dengan nama sesuai hari ini
3. Jika valid:

   * Baca Excel
   * Insert ke SQL Server (cek duplikat by `id`)
   * Pindah file ke `/archive/`
4. Jika gagal dibaca:

   * Pindah ke `/error/`
5. Jika nama tidak valid:

   * Kirim email
   * Pindahkan ke `/error/`
6. Tulis log ke `/logs/process.log`

---

## ✉️ Notifikasi

Jika file tidak sesuai format `laporanDDMMYYYY.xlsx`, email akan dikirim ke `EMAIL_CONFIG['receiver_email']`.
