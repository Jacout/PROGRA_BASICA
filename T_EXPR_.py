import re #se usa para importar re

#manera de generar objeto

abril=re.compile(r"[i|I][n|N][i|I][^A-Za-z\n]+[f|F][i|I][n|N]")

bir=input("Ingresa una cadena")

dani=abril.findall(bir) #primer caracteres

print(dani)



#eNTRADA Y VALIDACION DE DATOS
import re
data=dict()
def validacion(Fecha,correo,telefono,departamento,numemp):
  fechaval=re.compile(r'(\d\d)(\/d\d)(\/d\d\d\d)')
  correoval=re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
  televal=re.compile(r'\d\d\d\d\d\d\d\d\d\d')
  depaval=re.compile(r'^\d{1,10}$')
  numempval=re.compile(r'^\d{4}\d{4}$')
  if not fechaval.match(Fecha):
    return False
  elif not correoval.match(correo):
    return False
  elif not televal.match(telefono):
    return False
  elif not depaval.match(departamento):
    return False
  elif not numempval.match(numemp):
    return False
  else:
    return True


def agregar_datos(diccionario, nombre, fechaNac, correo, telefono, departamento, empleado_numero):
    diccionario[nombre] = {
        "Fecha Nacimiento": fechaNac,
        "Correo Electrónico": correo,
        "Teléfono": telefono,
        "Departamento": departamento,
        "Numero de empleado": empleado_numero
    }

nombre = input("Ingrese su nombre")
fechaNac = input("Ingrese su fecha de nacimiento dd/mm/aaaa")
correo =input("Ingrese su correo")
tele = int(input("Ingrese su telefono de 10 digitos"))
departa= int(input("Ingrese su departamento"))
empleado_numero = int(input("Ingrese su numero de empleado"))

if validacion(fechaNac, correo,tele,departa, empleado_numero)==True:
  agregar_datos(data,nombre, fechaNac, correo, tele, departa, empleado_numero)
else:
  print("Revise sus datos")
