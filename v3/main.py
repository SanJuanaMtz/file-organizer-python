import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import shutil

ventana = tk.Tk()

ventana.title("File Organizer Pro")
ventana.geometry("600x400")

CARPETAS = {
    "Documents": [".pdf", ".docx", ".txt"],
    "Pictures": [".jpg", ".jpeg", ".png"],
    "Compressed": [".zip", ".rar"]
}

carpeta_seleccionada = ""

def seleccionar_carpeta():
    global carpeta_seleccionada

    carpeta_seleccionada = filedialog.askdirectory()

    etiqueta_carpeta.config(
        text=f"Selected Folder: {carpeta_seleccionada}"
    )

def organizar_archivos():

    if not carpeta_seleccionada:
        messagebox.showwarning(
            "Warning",
            "Please select a folder first."
        )
        return

    for archivo in os.listdir(carpeta_seleccionada):

        ruta_archivo = os.path.join(
            carpeta_seleccionada,
            archivo
        )

        if os.path.isfile(ruta_archivo):

            extension = os.path.splitext(
                archivo
            )[1].lower()

            for carpeta_destino, extensiones in CARPETAS.items():

                if extension in extensiones:

                    destino = os.path.join(
                        carpeta_seleccionada,
                        carpeta_destino
                    )

                    os.makedirs(destino, exist_ok=True)

                    shutil.move(
                        ruta_archivo,
                        os.path.join(destino, archivo)
                    )

                    log_text.insert(
                        tk.END,
                        f"Moved: {archivo} → {carpeta_destino}\n"
                    )

                    break

    messagebox.showinfo(
        "Success",
        "Files organized successfully!"
    )

boton_seleccionar = tk.Button(
    ventana,
    text="Select Folder",
    command=seleccionar_carpeta
)

boton_seleccionar.pack(pady=10)

boton_organizar = tk.Button(
    ventana,
    text="Organize Files",
    command=organizar_archivos
)

boton_organizar.pack(pady=10)

etiqueta_carpeta = tk.Label(
    ventana,
    text="No folder selected"
)

etiqueta_carpeta.pack(pady=10)

log_text = tk.Text(
    ventana,
    height=10,
    width=60
)

log_text.pack(pady=10)

ventana.mainloop()
