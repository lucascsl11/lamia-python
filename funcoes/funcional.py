def soma(a, b):
    return a + b

# s = soma
# print(s(3,4))

# É possível passar uma função como parâmetro
# def somaExterna(fn, a, b):
#     return fn(a, b)

# resultado = somaExterna(soma, 3, 4)
# print(resultado)

# Função parcial
def soma_parcial(a):
    #Assumindo que haja processamento pesado aqui dentro, não precisamos repetir ele o tempo todo
    #Podemos criar uma função interna que faz o processamento mais leve e retorna o resultado
    #Assim, o tempo não se torna 3x a função externa, mas sim 1x a função externa e 3x a função interna (menor)
    def soma_interna(b):
        return a + b
    return soma_interna

s = soma_parcial(3)
print(s(4))

#ou podemos fazer tudo em uma linha
print(soma_parcial(3)(4))