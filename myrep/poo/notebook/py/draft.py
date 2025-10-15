Class Notebook:
	def __init__(self):
		self.__ligado: bool = false
		self.__bateria: Bateria | None = none
		self.__carregador: Carregador | None = none

	def __str__(self):
		return f"ligar {self.__ligado} bateria {self.__bateria}"
	
	def ligar(self):
		if self.__ligado:
			print("Notebook ligado")
		else:
			print("Notebook desligado")

	def usar(self, tempo: int):
		if tempo > self.__bateria:
			print(f"usado por {self.__bateria} minutos")
			return

	def mostrar(self):


Class Bateria:
    def __init__(self, capacidade):
        self.__capacidade: int = capacidade
        self.__carga: int = capacidade

	def mostrar(self):
		print(f"Bateria: {self.carga} {self.__capacidade")

    def __str__(self) -> str:
		return f"Bateria: {self.carga} {self.__capacidade}"

Class Carregador:
	def __init__(self, potencia: int):
		self.__potencia: int = potencia

	def mostrar(self):
        print(f"Carregador: (Potência {self.__potencia})")