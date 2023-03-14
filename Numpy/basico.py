"""
Como o Numpy funciona?

Library de arrays multidimensionais -> dá pra armazenar dados em arrays de vários tipos de dimensão
(1D, 2D, 3D, etc)

Por que usar numpy acima de listas? É simplesmente mais rápido.
    - Numpy usa tipos fixos de dados, enquanto listas usam tipos dinâmicos
    - Numpy faz um casting pra int32, int16 ou até int8
    - Enquanto isso Lists usam mais memória porque tem que armazenar muito mais informações sobre
    o dado que está sendo utilizado (tamanho, referencias, tipo e valor do objeto)
    descrita como um long ao invés de um int32
    - menos memória utilizada no total
    - no array, não tem que fazer type checking enquanto rola iteração
    já que em listas tem vários tipos
    - Memória contígua no Numpy enquanto lists usa memória espalhada
        - a memória contígua permite processamento SIMD (single instruction, multiple data)
        - uso de cache mais rápido, podemos manter os valores perto de onde é necessário acessar

Em listas e em Numpy podemos fazer inserção, delete, append, concat e etc, mas em Numpy podemos
fazer mais ainda

APLICAÇÕES
    - Matemática, pode ajudar a substituir o matlab
    - Plotagem de gráficos
    - Backend (Pandas lib) --> dá pra armazenar imagens e informação
    - Machine Learning (tensor lib)
"""

import numpy as np
import sys

a = np.array([1, 3, 5], dtype='int16')
# b = np.array([1,2,3])

# print(a * b)

# Array bidimensional
# c = np.array([[1,2,3], [4,5,6]], dtype= 'int16')
print(a)
print('O tamanho do array a é', a.ndim)  # Pegando a dimensão do array
# Pegando a forma do array (linhas, colunas)
print('A forma do array a é', a.shape)
# print('A forma do array a é' , a.shape) --> # Aqui só pega linhas porque o array é unidimensional
print('O tipo do array a é', a.dtype)  # Pegando o tipo de dado do array
# Pegando o tamanho dos ITENS do array em bytes
print('O tamanho do array a é', a.itemsize, 'bytes')
# Pegando a quantidade de itens do array
print('A quantidade de itens do array a é', a.size, 'itens')
# Tamanho total do array em bytes utilizando o nbytes (mesma coisa que itemsize * size)
print('O tamanho total do array a é', a.nbytes, 'bytes')

