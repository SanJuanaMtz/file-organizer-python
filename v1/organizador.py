import os #Read files
import shutil  #Move those files

carpeta = "Downloads"

for archivo in os.listdir(carpeta):
    if archivo.endswith(".pdf"):
        os.makedirs("Documents", exist_ok=True)
        shutil.move(f"{carpeta}/{archivo}", "Documents")

    elif archivo.endswith(".jpg"):
        os.makedirs("Pictures", exist_ok=True)
        shutil.move(f"{carpeta}/{archivo}", "Pictures")

    elif archivo.endswith(".docx"):
        os.makedirs("Documents", exist_ok=True)
        shutil.move(f"{carpeta}/{archivo}", "Documents")
