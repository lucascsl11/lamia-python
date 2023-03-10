class Carro:
    def __init__(self):
        self.__velocidade = 0

    @property
    def velocidade(self):
        return self.__velocidade
    
    def acelerar(self):
        self.__velocidade += 2
        return self.__velocidade

    def frear(self):
        self.__velocidade -= 2
        return self.__velocidade
    
class Uno(Carro):
    pass # Uno herda tudo de Carro

class Ferrari(Carro):
    def acelerar(self):
        super().acelerar() # Chama o método da classe pai
        return super().acelerar() # (no python, super tem que ter parênteses.)
    
c1 = Uno()
print(c1.acelerar())

c2 = Ferrari()
print(c2.acelerar())
print(c2.acelerar())