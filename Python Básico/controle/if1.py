aluno = {
    'nome': 'Lucas',
    'notas':{
        'CDI': 9,
        'POO': 1,
        'BD': 1
    }
}

# aluno['notas']['CDI'] = float(input('Digite a nota de CDI: '))
# isso não funciona porque conjunto não suporta atribuição de item

if(aluno['notas']['CDI'] >= 9):
    print('Aprovado com louvor em CDI')
elif(aluno['notas']['CDI'] >= 6):
    print('Aprovado em CDI')
else:
    print('Reprovado em CDI')