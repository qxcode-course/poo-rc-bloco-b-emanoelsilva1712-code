class Camisa:
    def __int__(self):
        self.__tamanho = 0

    def getTamanho(self) -> str:
        return self.__tamanho

    def setTamanho(self, valor: str):

        if valor == "PP" "P" "M" "G" "GG" "XG":
            retrun
        else:
            print("fail: Digite o tamanho da Camisa entre PP, P, M, G, GG, XG")


Camisa = roupa()
while roupa.getTamanho() == " ":

    print("Digite seu tamanho de roupa")
    tamanho = input()
    roupa.setTamanho(tamanho)

print(f"Parabens, voce comprou uma roupa {tamanho}", roupa.getTamanho())