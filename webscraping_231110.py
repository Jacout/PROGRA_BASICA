import requests

from bs4 import BeautifulSoup as bs
#se importa beautifulSoup y lo guarda como un alias 
#pip install beautifulsoup4

#para trabajar con json se importa
import json


page = requests.get("https://www.cetesdirecto.com/sites/portal/inicio")
print(page.status_code)
#si es 200 si jala osea esta disponible la pagina

#http cat, es un cliente en linea para ver codigos de estados
#print(page.content)
#Analisis del contnido html de la pagina descargada
sopa = bs(page.content, "html.parser")

#el metodo prettify () convertira un arbol de beautiful soup en una cadena unicode con formato, con una linea separada para cada etiqueta y cadena

print(sopa.prettify())

po = sopa.find_all("p") #busca los parafos html p = paraprah

print("Se encontraron", len(po), "resultados tipo parrafo")
print("Accedos al parrafo [0]")
potext = po[0].get_text() #obtiene el texto del objeto encontrado
print(potext)


datos_JSON={
  "tamaño" : "mediana",
  "precio" : 464,
  "toppings" : ["Champiñones","queso extra", "peperroni"],
  "cliente" : {
    "nombre" : "Jacob",
    "edad" : 25,
    "direccion" : "Calle 5 # 5 - 35"
  }

}
#convertir cadena de caracteres de json a un diccionario
datos_diccionario = json.loads(datos_JSON)
print(datos_diccionario)
print(datos_diccionario["tamaño"])
print(datos_diccionario["cliente"]["nombre"])

#Obtener una cadena de caracteres a JSON
cliente_JSON= json.dupms(datos_JSON)

#PARA ORDENAR LAS CLAVES DUMPS(OBJT, KEYS=TRUE)

#https://swapi.dev
