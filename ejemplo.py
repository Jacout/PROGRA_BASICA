print("Hola we")

print("")

costoArt=float(input("Ingrese el costo del productor "))
cantiArt=int(input("Ingrese la cantidad de productos vendidos de "))
ingreso=float(input("Con cuanto pago el cliente?"))

subtotal=costoArt*cantiArt
iva=subtotal*.16
total=subtotal+iva

cambio=ingreso-total

print("H organizacion S.A. de C.V")
print("RFC: HSAOA02736GC75")
print("Metodo de pago: Efectivo")
print("Pago inmediato")

print("CODIGO    CANTIDAD         DESCRIPCION      PRECIO UNITARIO     SUBTOTAL")
print("15784      ", cantiArt,"      Verificacion vehicular      ",  costoArt, "          ", subtotal)


print("Subtotal: ", subtotal)
print("IVA: ", iva)
print("Total: ", total)
print("Efectivo: ", ingreso)
print("Cambio: ", cambio)