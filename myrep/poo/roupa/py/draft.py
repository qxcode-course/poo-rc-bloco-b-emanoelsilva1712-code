class Roupa:
    def __init__(self):
        self.__tamanho: str = ""

    def getTamanho(self) -> str:
        return self.__tamanho

    def setTamanho(self, valor: str):
        tam_valido = ["PP", "P", "M", "G", "GG", "XG"]

        if valor in tam_valido:
            self.__tamanho = valor
        else:
            print(f"fail: Valor inválido, tente PP, P, M, G, GG ou XG")

def main():
    roupa = Roupa()
    while True:

        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break

        elif args[0] == "show":
            tamanho = roupa.getTamanho()
            if tamanho == "":
                print("size: ()")
            else:
                print(f"size: ({tamanho})")

        elif args[0] == "size":
            if len(args) == 2:
                roupa.setTamanho(args[1])
            else:
                print("fail: use size: '<valor>'")

        else:
            print(f"fail: comando invalido")
    
main()   