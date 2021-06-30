import os

# INGRESAR PATH DONDE ESTAN LOS ARCHIVOS QUE QUIERES CAMBIAR EL NOMBRE DEL ARCHIVO
#"C:\Users\Usuario\Desktop\archivosCesar\265\431"
osPath = r"C:\Replace"
# INGRESAR
textoInit = input("Texto a cambiar: ")
textoChange = input("Texto nuevo: ")
count = 0
for file in os.listdir(osPath):
    if (textoInit in file):
        name = file
        newName = name.replace(textoInit, textoChange)
        os.rename(osPath + "/" + file, osPath + "/" + newName)
        count = count + 1

print(count, "Nombres de archivos cambiados")
