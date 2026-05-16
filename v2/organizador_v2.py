import os
import shutil

carpeta = "Downloads"

CARPETAS = {
    "Documents": [".pdf", ".docx", ".txt"],
    "Pictures": [".jpg", ".jpeg", ".png"],
    "Compressed": [".zip", ".rar"]
}

for archivo in os.listdir(carpeta):

    ruta_archivo = os.path.join(carpeta, archivo)

    if os.path.isfile(ruta_archivo):

        extension = os.path.splitext(archivo)[1].lower()

        for carpeta_destino, extensiones in CARPETAS.items():

            if extension in extensiones:

                os.makedirs(carpeta_destino, exist_ok=True)

                shutil.move(
                    ruta_archivo,
                    os.path.join(carpeta_destino, archivo)
                )

                print(f"Moved: {archivo} → {carpeta_destino}")

                break