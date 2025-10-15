class Camisa:
    def __int__(self):
        self.__tamanho = 0

    def getTamanho(self) -> str:
        return self.__tamanho

    def setTamanho(self, tam: str):

        if tam=="PP" or tam=="P" or tam=="M" or tam=="G" or tam=="GG" or tam=="XG":
            self.___tamanho=tam
        return
    print("tamanho inválido")

    def set_tamanho(self):
        return felf.__tamanho

def main():
    camisa = Camisa()
    while True:
        n= input()
        camisa.set_Tamanho(n)
        if camisa.get_Tamanho() !="":
            break
    print(camisa)
main()