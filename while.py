# ESTRUTURA DE REPETIÇÃO WHILE

# num = 1

# while (num <= 10):
#     print(num)
#     num += 1
# print('Laço encerrado!')

#_______________________________________________________________________________________________________________________________________________________________

#Exemplo para quando eu não souber quantas vezes o laço vai executar, mas ele tem que ficar repetindo os comandos/instruções

nome = None

while True:
    print('Digite seu nome, ou x para parar:')
    nome = input()
    if nome == 'x' or nome == 'X':
        break
    print(f'Bem-vindo, {nome}')