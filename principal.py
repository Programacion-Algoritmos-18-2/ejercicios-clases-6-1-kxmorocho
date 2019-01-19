from paquete_archivos.mi_archivo import *
from busquedas.busqueda_binaria import busqueda_binaria
"""creacion de objeto para abrir archivo datos"""
data = MiArchivo()

datos = data.obtener_informacion() #se obtiene la info de datos.txt

datos = [dat.split(",") for dat in datos] #se separa cada linea del archivo con comas

datos1 = [] # se crea un arreglo nuevo
elementoBusqueda = 3
#se recorre el arreglo con un for
for x in datos:
	for dat in x:
		datos1.append((dat))

#se crea un objeto con la data final
arregloBusqueda = busqueda_binaria(datos1)
print (datos1)
arregloBusqueda.ordenarArreglo()

posicion = arregloBusqueda.busqueda_binaria(elementoBusqueda)
if (posicion == - 1):
	print("El entero"+ elementoBusqueda + "no se encontró")
else:
	print("El entero"+ elementoBusqueda + "se encontró en la posicion"+ posicion)