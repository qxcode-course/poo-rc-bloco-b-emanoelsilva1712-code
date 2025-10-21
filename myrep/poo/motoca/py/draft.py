class Pessoa:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__age = int
        
    def getAge(self):
        return (age)

    def getName(self):
        return (nome)

    def toString(self):
        return ("self.__nome:self.__age")


class Moto:
    def __init__(self):
        self.__potencia = 1
        self.__tempo: int = 0
        self.__pessoa: pessoa | Nome = Nome #pode ser uma pessoa ou pode ser nulo

    def add_pessoa(self, pessoa: Pessoa) -> bool:
        if self.__pessoa != none:
            print("um pessoa na moto")
            return False
        self.__pessoa = pessoa
        return True

    def remov(self) -> Pessoa | Nome:        #tiro a pessoa da moto
        aux = self.__pessoa
        self.__pessoa = None       #Se for = a nada, então retirou
        return aux          #retorna o auxiliar, que não tem ninguem

    def comprar_tempo(self, tempo: int):
        self.__tempo += tempo

    def dirigir(self, tempo: int) -> bool:
        if self.__tempo == 0:
            print("fail: não possui tempo")
            return 

        elif self.__tempo < tempo:
            print(f"fail: time finished after {self.__tempo} minutes")
            self.__tempo = 0

        elif self.__tempo >= tempo:
            self.__tempo -= tempo

    # retorna o som da buzina da moto
    def buzinar(self) -> str:
        som: str = "p"
        #de acordo com a potencia, vou adicionando um 'e' na variavel som
        for i in range(self.__potencia): #é assim que se faz o "for"
            som += "e"
        som += "m"
        return som


def main():
    moto = Moto()

    while True:
        #entrada do usuario
        line = input()
        #printar oque o usuario escreveu acima com um cifrao na frente
        print("$" + line)
        #divide a variavel line em uma lista separada por espaço
        args = line.split(" ")

        if args[0] == "end":
            break     

        elif args[0] == "show":
            print(f"power:{self.__potencia}, time:{self.__tempo}, person:{self.__pessoa}")   

        elif args[0] == "init":
            

        elif args[0] == "enter":
            nome = args[1] # tem as variaveis
            pessoa = Pessoa(nome) #tem as pessoa
            moto.inserir(pessoa) #manda as pessoas entrarem na moto

        elif args[0] == "leave":
            pessoa = moto.remover()
            if pessoa == None:
                print("ninguem na moto")
            else:
                print(f"{pessoa} saiu")
        
        elif args[0] == "buy":
             

        elif args[0] == "drive":

        elif args[0] == "honk":


main()