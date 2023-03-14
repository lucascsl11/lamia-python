def funcaoQueDáOi():
    print("Oi!")

# o que é o def?
# é uma palavra reservada que define uma função

# Funções podem ter parâmetros padrão que são utilizados quando nenhum outro parâmetro é passado


def oiCustomizado(nome='nome'):
    print("Oi, " + nome)

# python não tem sobrecarga de funções, ou seja, não é possível ter duas funções com o mesmo nome,
# mas com parâmetros diferentes


# quando importado, essa linha diz 'funcoes.basico' que é o caminho dela
# mas quando este arquivo é executado diretamente, é chamado de main
print(__name__)

# Podemos assim criar um controle de execução de funções para apenas acontecerem
# quando esse arquivo for executado diretamente

if __name__ == '__main__':
    print('Executando o arquivo basico.py')

def multiplicaESoma(a, b, c):
    return a + b * c