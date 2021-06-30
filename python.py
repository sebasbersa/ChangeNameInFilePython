import os

# INGRESAR PATH DONDE ESTAN LOS ARCHIVOS QUE QUIERES CAMBIAR EL NOMBRE DEL ARCHIVO
path = "C:\Users\Usuario\Desktop\archivosCesar\265\265"
osPath = r + path
# INGRESAR
textoInit = "265"
textoChange = "431"
count = 0
for file in os.listdir(osPath):
    if (textoInit in file):
        name = file
        newName = name.replace(textoInit, textoChange)
        os.rename(osPath + "/" + file, osPath + "/" + newName)
        count = count + 1

print(count, "nombres de archivos cambiados")
