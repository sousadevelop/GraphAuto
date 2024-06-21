import os
import shutil
import subprocess
import tempfile
from pathlib import Path
import ctypes
import tkinter as tk
from tkinter import ttk, messagebox

def clear_temp_files():
    temp_paths = [
        os.path.join(tempfile.gettempdir()),
        os.path.join(os.getenv('WINDIR'), 'Temp')
    ]

    for path in temp_paths:
        if os.path.exists(path):
            print(f"Apagando arquivos temporários em {path}")
            for root, dirs, files in os.walk(path):
                for file in files:
                    try:
                        os.remove(os.path.join(root, file))
                    except Exception as e:
                        pass
                for dir in dirs:
                    try:
                        shutil.rmtree(os.path.join(root, dir))
                    except Exception as e:
                        pass
    messagebox.showinfo("Concluído", "Arquivos temporários apagados com sucesso!")

def perform_windows_update():
    print("Iniciando o Windows Update")
    try:
        subprocess.run(["powershell", "Install-Module PSWindowsUpdate -Force -SkipPublisherCheck -Scope CurrentUser"], check=True)
        subprocess.run(["powershell", "Import-Module PSWindowsUpdate"], check=True)
        subprocess.run(["powershell", "Get-WindowsUpdate -Install -AcceptAll -AutoReboot"], check=True)
        messagebox.showinfo("Concluído", "Windows Update realizado com sucesso!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro", f"Erro ao executar o Windows Update: {e}")

def clear_recycle_bin():
    print("Esvaziando a lixeira")
    try:
        ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 0x00000001)
        messagebox.showinfo("Concluído", "Lixeira esvaziada com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao esvaziar a lixeira: {e}")

def defragment_drive():
    drive = "C:"  # Defina o drive que deseja desfragmentar
    print(f"Desfragmentando o drive {drive}")
    try:
        subprocess.run(["defrag", drive, "/O", "/H", "/V"], check=True)
        messagebox.showinfo("Concluído", "Desfragmentação concluída com sucesso!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro", f"Erro ao desfragmentar o drive: {e}")

# Configurando a interface gráfica
root = tk.Tk()
root.title("Manutenção do Sistema")
root.geometry("800x800")  # Aumente o tamanho da janela para garantir espaço suficiente

# Definindo ícones -- opicional
#root.iconbitmap(".\\assets\icons\\icon_desejado.ico")


# Estilos
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 10))
style.configure("TLabel", font=("Helvetica", 12))

frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

# Configurando a coluna para expandir e centralizar widgets
frame.grid_columnconfigure(0, weight=1)

# Adicionando os botões com ícones
clear_temp_icon = tk.PhotoImage(file='C:\\Users\\victt\\OneDrive\\Imagens\\icons\\limpar.png')
clear_temp_icon = clear_temp_icon.subsample(5, 5)  # Reduz para metade do tamanho original
btn_clear_temp = ttk.Button(frame, text="Apagar Arquivos Temporários", image=clear_temp_icon, compound=tk.LEFT, command=clear_temp_files)
btn_clear_temp.grid(row=0, column=0, pady=5, sticky="ew")

windows_update_icon = tk.PhotoImage(file='C:\\Users\\victt\\OneDrive\\Imagens\\icons\\atualizacao-do-calendario.png')
windows_update_icon = windows_update_icon.subsample(5, 5)  # Reduz para metade do tamanho original
btn_windows_update = ttk.Button(frame, text="Realizar Windows Update", image=windows_update_icon, compound=tk.LEFT, command=perform_windows_update)
btn_windows_update.grid(row=1, column=0, pady=5, sticky="ew")

recycle_bin_icon = tk.PhotoImage(file='C:\\Users\\victt\\OneDrive\\Imagens\\icons\\restauracao-de-lixo.png')
recycle_bin_icon = recycle_bin_icon.subsample(5, 5)  # Reduz para metade do tamanho original
btn_clear_recycle_bin = ttk.Button(frame, text="Esvaziar Lixeira", image=recycle_bin_icon, compound=tk.LEFT, command=clear_recycle_bin)
btn_clear_recycle_bin.grid(row=2, column=0, pady=5, sticky="ew")

defragment_icon = tk.PhotoImage(file='C:\\Users\\victt\\OneDrive\\Imagens\\icons\\curativo.png')
defragment_icon = defragment_icon.subsample(5, 5)  # Reduz para metade do tamanho original
btn_defragment_drive = ttk.Button(frame, text="Desfragmentar Disco", image=defragment_icon, compound=tk.LEFT, command=defragment_drive)
btn_defragment_drive.grid(row=3, column=0, pady=5, sticky="ew")

btn_exit = ttk.Button(frame, text="Sair", command=root.quit)
btn_exit.grid(row=4, column=0, pady=20, sticky="ew")

root.mainloop()

################################
## Signature: João Victor S.S.##
################################