class Produto:
    # Método construtor
    def __init__(self, nome, preco = 1):
        self.__nome = nome #Uso de __ para tornar o atributo privado
        self.__preco = preco

    # Devemos sempre passar 'self' como primeiro parâmetro, pois ele representa o objeto
    @property # Decorator que transforma o método em um atributo, não precisando usar os parênteses
    def promocao(self):
        return self.preco * 0.9
    
    # Getter para atributo privado
    @property
    def getNome(self):
        return self.__nome
    
    @property
    def getPreco(self):
        return self.__preco
    
    #Setter para atributo privado
    @getPreco.setter
    def preco(self, preco):
        self.__preco = preco

# Diferente de Java, não precisamos da palavra-chave 'new' para instanciar um objeto
p1 = Produto('Caneta')
p2 = Produto('Lápis', 0.99)

print(p1._Produto__nome, p1.preco) # Acessando atributo privado com o nome da classe também funciona
# Mas o getter é divertido
print(p2.getNome, p2.preco)

# Graças ao @property podemos acessar a função como um atributo
print(p1.getNome, p1.promocao)

# Não precisamos chamar o setter, podemos simplesmente atribuir um valor ao atributo
p1.preco = 2.99
print(p1.getNome, p1.getPreco)