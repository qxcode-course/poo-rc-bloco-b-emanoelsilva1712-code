class Chinela:
    def __init__(self):
        self.__tamanho: int = 0

    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, novo_tamanho):
        if not isinstance(novo_tamanho, int):
            print(f"ERRO: '{novo_tamanho}' não é um número inteiro válido.")
            return False

        if not (20 <= novo_tamanho <= 50):
            print(f"ERRO: O tamanho {novo_tamanho} está fora do intervalo permitido. Deve ser entre 20 e 50.")
            return False
        
        if novo_tamanho % 2 != 0:
            print(f"ERRO: O tamanho {novo_tamanho} não é um número par. O tamanho da chinela deve ser par.")
            return False

        self.__tamanho = novo_tamanho
        return True

chinela = Chinela()
print("--- Validador de Tamanho de Chinela ---")
print("Regra: Tamanho deve ser um número PAR entre 20 e 50.\n")

while chinela.getTamanho() == 0:
        entrada = input("Digite seu tamanho de chinela: ")
        tamanho = int(entrada)
        
        if chinela.setTamanho(tamanho):
            print(f"\nSUCESSO! Você comprou uma chinela tamanho {chinela.getTamanho()}.")
