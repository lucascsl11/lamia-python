# for i in range(1, 10, 2):
#     print(i)

# for i in range(30, 0, -5):
#     print(i)

# nums = [10, 20, 30, 40]
# for n in nums:
#     print(n, end=' ')

palavra = 'ABCDEFGHI'
for caracter in palavra:
    if caracter == palavra[-1]:
        print(caracter, end = '\n')
    else:
        print(caracter, end=', ')

dicionario = {
    'nome': 'a',
    'numero': 1
}
for item in dicionario:
    print(item, ":", dicionario[item]) #printa as chaves e os valores

#outro jeito de resolver isso
for atributo, valor in dicionario.items():
    print(atributo, ":", valor)

#imprimindo os valores de um dicionário
for valor in dicionario.values():
    print(valor)

#imprimindo as chaves de um dicionário
for chave in dicionario.keys():
    print(chave)

for letra in {'a', 'b', 'c', 'd'}:
    print(letra, end = ' ') #loops em conjuntos trabalham em ordem aleatória!
    # isso aqui pode printar a b c d, a c d b, d c a b, etc.

