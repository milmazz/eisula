class postgrado:
	"Clase Postgrado"
	def __init__(self,_location="UNKNOWN",_degree="UNKNOWN",_dpto=0):
		#Constructor de la clase
		self.location = _location
		self.degree = _degree
		self.dpto = _dpto
	
	def set_location(self,_location):
		#Cambia el valor de la ubicacion del postgrado por el dado
		self.location = _location
	
	def set_degree(self,_degree):
		#Cambia el titulo obtenido por el dado
		self.degree = _degree
		
	def set_dpto(self,_dpto):
		#Asigna el Departamento al que esta adscrito el Postgrado
		self.dpto=_dpto
	
	def get_location(self):
		#Devuelve la ubicacion del postgrado
		return self.location
		
	def get_degree(self):
		#Devuelve el titulo obtenido
		return self.degree
		
	def get_dpto(self):
		#Devuelve el idntificador del Departamento al que esta adscrito el Postgrado
		return self.dpto
	
	def display(self):
		#Imprime Los atributos de la clase
		print self.__doc__
		print self.get_location()
		print self.get_degree()
		print self.get_dpto()