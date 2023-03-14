#Podemos passar quantos números forem desejados utilizando isso, mas eles serão passados como tupla
def soma (*nums):
    total = 0
    for n in nums:
        if(n == 0):
            return total #da até pra meter o louco com recursão aqui
        total += n
    #seria possível só colocar total += n sem critério de parada
    #mas eu resolvi dar uma brincadinha

#Kwargs é um dicionário de argumentos nomeados, que pode ser acessado como se fosse objeto
#pra pegar as informações (diferente de Java, não se acessa com . e sim com [])
#Esse processo com kwargs se chama packing
def result(**kwargs):
    status = 'Aprovado' if kwargs['nota'] >= 6 else 'Reprovado'
    print(f'{kwargs["nome"]} está {status} com nota {kwargs["nota"]}')