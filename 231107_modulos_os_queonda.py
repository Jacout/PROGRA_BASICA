import os
 #libreria que proporciona metodos para abrir y tener acceso a los archivos

c=0

for dirpath, dirnames, filenames in os.walk("C:\\Users\\Dell\\Downloads"):#genera los nombres del directorio caminanaod del arbol desde la parte mas alta hasta la mas baja
  #regresa una tupla

  for name in filenames:
    if ".txt" in name:
      print("Archivos", c, ":", os.path.join(dirpath, name))
      print("El contenido del archivo es: ")
      fo = open(os.path.join(dirpath,name),"r")
      for line in fo:
        print(line)
      fo.close()
      c+=1


print("A")

milista=os.listdir(path="C:\\Users\\Dell\\Downloads")
print(milista)
