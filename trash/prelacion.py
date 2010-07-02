#Toda la clase se especifica basada en el esquema 'A' prela a 'B'
class prelacion:
	"Clase Prelacion (Relacion n-n de materias)"
	def __init__(self,_prelador=0,_prelada=0):
		#Constructor de la Clase
		self.prelador = _prelador
		self.prelada = _prelada
		
	def set_prelador(self,_prelador):
		#Asigna el valor de la materia A
		self.prelador = _prelador
	
	def set_prelada(self,_prelada):
		#Asigna el valor de la materia B
		self.prelada = _prelada
		
	def get_prelador(self):
		#Devuelve el valor de A
		return self.prelador
		
	def get_prelada(self):
		#Devuelve el valor de B
		return self.prelada
		
	def display(self):
		#Imprime los atributos de la clase
		print self.get_prelador(),"-->",self.get_prelada()