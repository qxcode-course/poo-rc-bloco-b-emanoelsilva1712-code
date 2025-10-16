class Chinela:
    def __init__(self):
        self.__tamanho: int=0

    def get_tamanho(self) -> int:
        return self.__tamanho

    def __str__(self)->str:
        return f"sua chinela é tamanho: {self.__tamanho}"

    def set_tamanho(self, tam:int) -> None:
        if tam>=20 and tam<=50 and tam%2==0:
            self.__tamanho=tam
            return
        print("tamanho invalido")

def main():
    chinela=Chinela()
    while True:
        n=int(input())
        chinela.set_tamanho(n)
        if chinela.get_tamanho()!=0:
            break
    print("chinela")


main()