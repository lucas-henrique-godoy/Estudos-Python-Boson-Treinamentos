# FUNÇÃO PRINT() E COMO FORMATAR A SAÍDA

# Sintaxe: 
# print(objetos, argumentos)
# A função print() é usada para exibir mensagens ou valores no console. Ela pode receber vários argumentos separados por vírgula.

#_______________________________________________________________________________________________________________

# Exemplo básico de uso da função print():
mensagem = 'Função print()'
print(mensagem)  # Imprime 'Função print()' no console
print('Aula de Python')  # Imprime 'Aula de Python' no console

#_______________________________________________________________________________________________________________

# Concatenação de strings usando print():
nome = 'Lucas Henrique Godoy'
canal = 'Bóson Treinamentos'
print(canal, '-', nome)  # Imprime 'Bóson Treinamentos - Lucas Henrique Godoy' no console

#_______________________________________________________________________________________________________________

# Usando input() para capturar entrada do usuário e formatando a saída:
nome = input('Digite seu nome: ')  # Solicita ao usuário que digite seu nome
msg = 'Olá ' + nome + '! Bem-vindo ao curso de Python!'
print(msg)  # Imprime a mensagem de boas-vindas com o nome inserido pelo usuário

# OU usando concatenação diretamente na função print():
print('Olá ' + nome + '! Bem-vindo ao curso de Python!')  # Versão simplificada da mensagem de boas-vindas

print('Outro texto')  # Imprime 'Outro texto' em uma nova linha

#_______________________________________________________________________________________________________________

# Modificando o comportamento de quebra de linha usando o argumento end:
print('Imprime a mensagem e muda de linha')
print('Imprime a mensagem e permanece na linha.', end='')  # Não muda de linha após essa mensagem
print(' Continuo na mesma linha!')  # Continua na mesma linha da mensagem anterior

#_______________________________________________________________________________________________________________

# Utilizando formatação de string com o método format():
nome = 'Maria'
idade = 30
print('O nome dela é {0} e ela tem {1} anos'.format(nome, idade))  
# Imprime usando formatação com índices: 'O nome dela é Maria e ela tem 30 anos'

# OU usando uma variável para armazenar a mensagem formatada:
msg_formatada = 'O nome dela é {0} e ela tem {1} anos'.format(nome, idade)
print(msg_formatada)  # Imprime a mensagem formatada armazenada na variável

#_______________________________________________________________________________________________________________

# F STRING: forma moderna de formatação de strings introduzida no Python 3.6
nome = 'Lucas'
peso = 67.10
print(f'Olá, meu nome é {nome} e meu peso é {peso} quilos')  
# Utilizando f-string para formatar a mensagem: 'Olá, meu nome é Lucas e meu peso é 67.1 quilos'

# OU armazenando a mensagem em uma variável:
msg = f'Olá, meu nome é {nome} e meu peso é {peso} quilos.'
print(msg)  # Imprime a mensagem formatada armazenada na variável

#_______________________________________________________________________________________________________________

# F STRING EXECUTANDO OPERAÇÕES: é possível realizar operações dentro de uma f-string
a = 10
b = 5
res = f'A soma de {a} com {b} é igual a: {a + b}'  
print(res)  # Imprime a mensagem com o resultado da operação dentro da f-string: 'A soma de 10 com 5 é igual a: 15'

#_______________________________________________________________________________________________________________

# F STRING EXECUTANDO OPERAÇÕES. EXEMPLO 2: formatação de números com f-string
valor = 125.579637
print(f'O valor é: {valor:.2f}')  
# Imprime o valor arredondado com duas casas decimais: 'O valor é: 125.58'

#_______________________________________________________________________________________________________________

# CARACTERE DE ESCAPE: uso de caracteres de escape em f-strings
valor = 125.579637
print(f'O valor é: \'{valor:.2f}\'')  
# Imprime o valor entre aspas simples usando o caractere de escape \': 'O valor é: '125.58''
# Caso seja necessário mostrar numa situação o caractere de \ é só usar \\ para mostrar 1 barra.

#_______________________________________________________________________________________________________________

# CARACTERE DE ESCAPE - TABULAÇÃO \t: uso do caractere de escape \t para tabulação
nome = 'Lucas'
idade = 26
print(f'Nome: {nome}\tIdade: {idade}')  
# Imprime nome e idade separados por uma tabulação: 'Nome: Lucas    Idade: 26'
