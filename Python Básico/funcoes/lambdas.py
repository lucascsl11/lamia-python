from functools import reduce

alunos = [
    {'nome': 'João', 'nota': 1},
    {'nome': 'Maria', 'nota': 2},
    {'nome': 'Pedro', 'nota': 8},
    {'nome': 'Ana', 'nota': 7},
]

# Filtrando elementos dentro de uma lista com lambda e filter
# Lambda é uma função anônima, ou seja, sem nome, que pode ser definida rapidamente em 1 linha


def aluno_aprovado(aluno): return aluno['nota'] >= 6
# Aluno é o parâmetro que será passado para a função lambda
# Tudo que tiver depois do : é o retorno da função lambda

# Passando para o filter ---> tem que colocar list() antes do filter para transformar o filter em uma lista
# Senão ele vai printar um endereço de memória


# Filter basicamente passa os elementos da lista pela função lambda que os filtra e dá o resultado final
# Se 'aluno_aprovado' for True, ele vai adicionar o elemento na lista
# Se 'aluno_aprovado' for False, ele vai ignorar o elemento
alunos_aprovados = (filter(aluno_aprovado, alunos))

# Outro exemplo de lambda
obter_nota = lambda aluno: aluno['nota']
for aluno in alunos:
    print(obter_nota(aluno))

notas_alunos_aprovados = list(map(obter_nota, alunos_aprovados))

print(notas_alunos_aprovados)

# alternativa sem usar lambda
# alunos_aprovados = [aluno for aluno in alunos if aluno['nota'] >= 6]
# notas_alunos_aprovados = [aluno['nota'] for aluno in alunos_aprovados]