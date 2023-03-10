x = 10

while(x):
    print(x, end=" ")
    x -= 1

correctPassword = 1234
passwordInput = int(input('Digite a senha: '))

while passwordInput != correctPassword:
    passwordInput = int(input('Senha incorreta.\nDigite a senha novamente: '))

print('Senha correta.')