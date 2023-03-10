print({1, 2, 3})
print(type({1, 2, 3}))
#set = conjunto

#não pode elemento duplicado em set!
set1 = {1, 2}
print(set1)

set1.add(1)
#isso aqui não funciona justamente por isso
print(set1)

"""
também não tem indexação em sets,
o que significa que não tem como acessar um elemento
a partir de valores indexados como set[0]
"""