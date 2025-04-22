ClaseIP = {
    1: [1962946, 'ALMAGUER ROBERTO'],
    2: [1757671, 'AVILA DIEGO OSVALDO'],
    3: [1540361, 'BOSQUES JACCELL'],
    4: [1648481, 'CABALLERO CESAR GIOVANI'],
    5: [1904860, 'ROSALES ERICK'],
    6: [1756284, 'SANTOS RAUL RICARDO'],
    7: [1940347, 'TAMEZ ALEJANDRA NOHEMI'],
    8: [1902125, 'TREJO LUIS ALBERTO'],
    9: [1777391, 'URESTI DIEGO TADEO'],
    10: [1945247, 'VALERIO FRANCISCO JAVIER'],
    11: [1504261, 'GONZÁLEZ SEBASTIÁN'],
    12: [1547820, 'GONZALEZ GUSTAVO DE JESUS'],
    13: [1842704, 'GUERRA MIGUEL ANGEL'],
    14: [1686563, 'HERNANDEZ JAIRO IVAN'],
    15: [1696484, 'HERNANDEZ JAIR CALEB'],
    16: [1902200, 'CANTU ALEJANDRA'],
    17: [1619624, 'CANTU BARBARA AZALIA'],
    18: [1455963, 'GARCIA OLAF ALIBER'],
    19: [1543305, 'GARCIA LUIS GUSTAVO'],
    20: [1982458, 'GONZALEZ AARON ADRIAN'],
    21: [1734585, 'GONZALEZ LUIS ADOLFO'],
    22: [1706896, 'NAVARRO YAHIR ALEJANDRO'],
    23: [1943702, 'NAVARRO DAVID ALEJANDRO'],
    24: [1406092, 'PEREZ JARED ABRAHAM'],
    25: [1914132, 'RIVERA JOSE EDUARDO'],
    26: [1570175, 'ROCHA ANGELA MARIA'],
    27: [1760363, 'RODRIGUEZ DEBORAH CANDOX'],
    28: [1785849, 'RODRIGUEZ REINALDO MANUEL'],
    29: [1702696, 'RODRIGUEZ CESAR ALEJANDRO'],
    30: [1978181, 'LARA DEYRON LEONARDO'],
    31: [1451339, 'LEZA DARIEN ALEJANDRO'],
    32: [1641777, 'LOZANO DANIEL ADRIAN'],
    33: [1700167, 'LUNA RAUL JAHZIEL'],
    34: [1590587, 'MANCHA DANIEL'],
    35: [1969246, 'MUÑOZ EDUARDO TADEO'],
}

# Función para comparar nombres 
def comparar_nombres(registro1, registro2):
    return registro1[1] > registro2[1]

# Ordenamiento de burbuja
def ordenar_por_nombre_burbuja(diccionario):
    n = len(diccionario)
    for i in range(n):
        for j in range(0, n-i-1):
            if comparar_nombres(diccionario[j], diccionario[j+1]):
                diccionario[j], diccionario[j+1] = diccionario[j+1], diccionario[j]

# Convertir el diccionario en una lista para poder ordenar
lista_registros = list(ClaseIP.values())

# Llamar a la función de ordenamiento
ordenar_por_nombre_burbuja(lista_registros)

# Convertir la lista ordenada de nuevo a un diccionario
ClaseIP_ordenado = {i+1: registro for i, registro in enumerate(lista_registros)}

# Imprimir el diccionario ordenado
for clave, valor in ClaseIP_ordenado.items():
    print(clave, valor)
