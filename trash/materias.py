class subject:
	"Clase Materias"
	def __init__(self,_name="UNKNOWN",_tced="UNKNOWN",_dpto=0,_pg=False):
		#Constructor de la clase
		self.name = _name
		self.tced = _tced
		self.pg = _pg
		self.dpto = _dpto
	
	def set_name(self,_name):
		#Cambia el valor del nombre de la materia al dado
		self.name = _name
	
	def set_tced(self,_tced):
		#Cambia el valor de la Cedula del profesor que imparte la materia al dado
		self.tced = _tced
		
	def set_pg(self,_pg):
		#Ajusta la variable pg de acuerdo a si pertenece o no al postgrado
		self.pg=_pg
		
	def set_dpto(self,_dpto):
		#Asigna el identificador del Departamento a la materia
		self.dpto = _dpto
	
	def get_name(self):
		#Devuelve el nombre de la materia
		return self.name
		
	def get_tced(self):
		#Devuelve la cedula del profesor que imparte la materia
		return self.tced
		
	def get_pg(self):
		#Devuelve la variable pg
		return self.pg
		
	def get_dpto(self):
		#Devuelve el identificador del departamento al que esta inscrita la materia
		return self.dpto
	
	def display(self):
		#Imprime Los atributos de la clase
		print self.__doc__
		print self.get_name()
		print self.get_tced()
		print self.get_dpto()
		if(not self.get_pg):
			print "Materia Pregrado"
		else:
			print "Materia Postgrado"