import os
import shutil

from_dir = ("C:/Users/Cliente/Downloads/")

to_dir = ("C:/Users/Cliente/Desktop/Projetos/Arquivos_Documentos/")

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    print(name)
    print(extension)
    if extension == " ":
        continue
    if extension in [".txt", ".doc", ".docx", ".pdf"]:
        path1 = from_dir+file_name
        path2 = to_dir+"Pastinha"
        path3 = to_dir+"Pastinha/"+file_name
        if os.path.exists(path2):
            print("Movendo"+ file_name)
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Movendo"+ file_name)
            shutil.move(path1, path3)

