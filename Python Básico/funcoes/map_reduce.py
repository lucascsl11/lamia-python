from functools import reduce

notas = [4.4, 3.3, 5.5, 6.6]

# for i, nota in enumerate(notas):
#     print (i, nota)

#Dá pra fazer isso de uma forma mais simples usando map
# def aumento_de_ponto(nota):
#     return nota + 1.5

# notasFinais = map(aumento_de_ponto, notas)
# print(list(notasFinais))  -----> se imprimir somente 'notas' vai imprimir o endereço de memória (curioso...)

#podemos fazer isso com criação de função também

def aumentaPonto(delta):
    def calculo(nota):
        return nota + delta
    return calculo

notasFinais = list(map(aumentaPonto(1.5), notas))
print(notasFinais)

#Usando reduce para calcular a soma de todas as notas
def somar(a, b):
    return a + b

print(reduce(somar, notas, 0)) #o 0 é o valor inicial da soma (se não colocar, ele pega o primeiro valor da lista como inicial)
# o que isso faz é pegar o primeiro valor da lista e somar com o segundo, 
# depois o resultado com o terceiro, e assim por diante