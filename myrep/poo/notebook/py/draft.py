Class Notebook:
	def __init__(self):
		self.__ligado: bool = False
		self.__bateria: Bateria | None = none
		self.__carregador: Carregador | None = none

	def __str__(self):
		return f"ligar {self.__ligado} bateria {self.__bateria}"
	
	def ligar(self, ligado):
		self.__ligado = True
		print("Notebook ligado")
	
	def desligar(self):
		self.__desligado = False
		print("Notebook desligado")

	def mostrar(self):
		print(f"Notebook: {self.ligado} {self.__bateria} {self.__carregador}")

	def usar(self, tempo: int):
		if tempo > self.__bateria:
			print(f"usado por {self.__bateria} minutos")
			return


Class Bateria:
    def __init__(self, capacidade: int):
        self.__capacidade: int = capacidade
        self.__carga: int = capacidade

	def getcapacidade(self) -> int:
		return self.__capacidade

	def getcarga(self) -> int:
		return self.__carga

	def carregar(self, valor: int):
		self.__carga = (self__carga + valor, self__capacidade):

	def descarregar(self, valor; int) -> int:
		carga_usada = (valor, self.__carga)
		self.__carga -= carga_usada
		return carga_usada

	def mostrar(self):
		print(f"Bateria: {self.carga} {self.__capacidade}")

    def __str__(self) -> str:
		return f"Bateria: {self.carga} {self.__capacidade}"


Class Carregador:
	def __init__(self, potencia: int):
		self.__potencia: int = potencia

	def getpotencia(self) -> int:
		return self.__potencia

	def mostrar(self):
        print(f"Carregador: (Potência {self.__potencia})")

	def __str__(self) -> str:
		return f"potencia {self.__potencia}"