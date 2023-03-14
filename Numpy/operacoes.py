import numpy as np

# a = np.array([[1,2,3,4,5,6,7], [4,5,6,7,8,9,10]])
# print(a)

# Pegando um elemento específico (linha, coluna)
# linha = int(input('Digite a linha: '))
# coluna = int(input('Digite a coluna: '))
# print('O', coluna, 'º elemento da', linha, 'º linha é', a[linha-1, coluna-1])
# Também podemos usar a notação de elemento negativo (-1, -2, etc)

# Pegando uma linha inteira (funciona da mesma forma que listas nos intervalos e usando :)
# print(a[0, :])
# Pegando uma coluna
# print(a[:, 3])

# Pegando um intervalo assim como funciona em listas (inicio:fim:stepsize)
# print(a[0, 1:6:2])

# Mudando um elemento específico
# a[1, 5] = 20
# print(a)

# Mudando uma linha inteira
# a[0, :] = [9,9,9,9,7,2,9]
# print(a)

# Array tridimensional
b = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
print(b)