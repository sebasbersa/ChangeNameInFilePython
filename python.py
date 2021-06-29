import os

osPath = r"C:\Users\Usuario\Desktop\archivosCesar\265\265"
count = 0
for file in os.listdir(osPath):
    if ("265" in file):
        name = file
        newName = name.replace("265", "431")
        os.rename(osPath + "/" + file, osPath + "/" + newName)
        count = count + 1

print(count, "nombres de archivos cambiados")

osPath = r"C:\Users\Usuario\Desktop\archivosCesar\265"
count = 0
for file in os.listdir(osPath):
    if ("265" in file):
        name = file
        newName = name.replace("265", "431")
        os.rename(osPath + "/" + file, osPath + "/" + newName)
        count = count + 1
        
print(count, "nombres de archivos cambiados")
