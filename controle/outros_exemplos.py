linha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
coluna = ['1', '2', '3', '4', '5', '6', '7', '8']

# print('Tabuleiro de xadrez\n')
# for i in linha:
#     for j in coluna:
#         print((i+j), end=' ')

# print('\n')

for i in [1,2,3]:
    pass   # pass é um comando que não faz nada, é só um placeholder

for caracter in 'NAO LEIA AS LETRAS E DESSA FRASE':
    if caracter == 'E':
        continue # continue faz o mesmo que o pass
    else:
        print(caracter, end='')

