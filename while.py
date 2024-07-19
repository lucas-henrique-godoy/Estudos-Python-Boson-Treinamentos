# Exemplo de estrutura de repetição while simples

num = 1  # Inicializa a variável num com o valor 1

while (num <= 10):  # Enquanto num for menor ou igual a 10, execute o bloco de código abaixo
    print(num)  # Imprime o valor atual de num
    num += 1  # Incrementa o valor de num em 1
print('Laço encerrado!')  # Após sair do laço, imprime esta mensagem


#_______________________________________________________________________________________________________________________________________________________________

#Exemplo para quando eu não souber quantas vezes o laço vai executar, mas ele tem que ficar repetindo os comandos/instruções

# Exemplo de estrutura de repetição while para entrada de dados indefinida

nome = None  # Inicializa a variável nome com None (nulo)

while True:  # Repete indefinidamente, a menos que seja interrompido por um break
    print('Digite seu nome, ou x para parar:')  # Solicita que o usuário digite um nome ou 'x' para parar
    nome = input()  # Captura a entrada do usuário e atribui a variável nome
    if nome == 'x' or nome == 'X':  # Verifica se o usuário digitou 'x' ou 'X'
        break  # Se sim, interrompe o laço
    print(f'Bem-vindo, {nome}')  # Se não, imprime uma mensagem de boas-vindas com o nome digitado
print('Até logo!')  # Após sair do laço, imprime esta mensagem
   