class ArregloBinario(object):
	"""docstring for ArregloBinario"""
	def __init__(self, datos):
		self.datos_ListArrayDatos = datos
	"""se agregan metodos para para agregar los datos del .txt a un arreglo """
	def agregarDatos(self, dat):
		self.datos_ListArrayDatos = dat 
	
	def obtenerDatos(self):
		return self.datos_ListArrayDatos
		"""se ordena los datos del arreglo"""
	def ordenarArreglo(self):
		self.datos_ListArrayDatos.sort()
"""Algoritmo de busqueda binaria"""
def busqueda_binaria(self, elementoBusqueda):
	"""declaracion de variables"""
	inferior = 0
	superior = len(arreglo) - 1
	medio = (inferior + superior) // 2
	ubicacion = -1
	while((inferior <= superior) and (ubicacion == -1)):
			
			if(elementoBusqueda == self.obtener_informacion()[medio]):
				ubicacion = medio

			else:
					if(elementoBusqueda < self.obtener_informacion()[medio]):
						superior = medio - 1

					else:
						inferior = medio + 1


			medio = int((inferior + superior + 1) / 2)
		

	return ubicacion
"""metoso tostring para presentar los dtos"""
def __toString__(self):
	c = ""
	for i in self.datos:
		c = "%s %d" + (c, i)
	return c
   


