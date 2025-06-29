import os
import subprocess
import sys
import platform

def create_virtual_env():
    print("Membuat ulang virtual environment...")
    subprocess.run([sys.executable, "-m", "venv", ".venv"])
    print("Virtual environment berhasil dibuat.")

def install_requirements():
    print("Menginstal dependencies dari requirements.txt...")
    pip_path = ".venv\\Scripts\\pip.exe" if platform.system() == "Windows" else ".venv/bin/pip"
    subprocess.run([pip_path, "install", "-r", "requirements.txt"])
    print("Semua dependensi berhasil diinstal.")

def main():
    if os.path.exists(".venv"):
        print("Folder .venv sudah ada, disarankan hapus terlebih dahulu jika ingin setup ulang.")
        jawab = input("Ingin hapus dan buat ulang .venv? (y/n): ").lower()
        if jawab == 'y':
            print("Menghapus folder .venv...")
            if platform.system() == "Windows":
                subprocess.run(["rmdir", "/S", "/Q", ".venv"], shell=True)
            else:
                subprocess.run(["rm", "-rf", ".venv"])
        else:
            print("Setup dibatalkan.")
            return

    create_virtual_env()
    install_requirements()
    print("Setup selesai. Silakan aktifkan environment:")
    if platform.system() == "Windows":
        print(".venv\\Scripts\\activate")
    else:
        print("source .venv/bin/activate")

if __name__ == "__main__":
    main()
