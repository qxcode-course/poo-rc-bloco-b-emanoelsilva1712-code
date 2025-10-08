class Chinela:
    def __init__(self):
        self.__tamanho: int = 0

    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, novo_tamanho):
        
        if novo__tamanho <= 20 and novo__tamanho >= 50:
            print("Erro, digite outro numero")
        else:
            print("Digite o tamanho da chinela")
        
        if novo__tamanho % 2 != 0:
            print("Erro, digite outro numero")
        else:
            print("Digite o tamanho da chinela")

while Chinela.getTamanho() == 0:
    print("Digite seu tamanho de chinela")
    tamanho = int(input())

    Chinela.setTamanho(tamanho)
    print(f"Parabens, voce comprou uma chinela tamanh{chinela.getTamanho()}")
    
        

