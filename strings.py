# STRINGS

# EXEMPLO 1
#nome = 'Curso de Python'
#instrutor = ' Fábio'
#letra = nome[2] # Mostra o valor que esta na posição 2 da frase na lista.
#print(letra)
#print(nome + ' com ' + instrutor) # Concatenando strings
#print(len(nome)) # Retorna o valor do comprimento da strings

#________________________________________________________________________________________________________________
# EXEMPLO 2
#frase = 'Vamos aprender python hoje.'
#palavras = frase.split() # Divide a string em partes, separadas por espaço por padrao criando assim uma lista de strings. Todas as palavras separadas por espaço se transformou em um item de uma lista, que agora podem ser acessados individualmente inclusive com [].
#print(palavras[1])
#________________________________________________________________________________________________________________

# Iterando sobre cada frase
# for palavra in palavras:
#     print(palavra)
#________________________________________________________________________________________________________________

# Iterando sobre cada letra 
# for letra in frase:
#     print(letra)

#________________________________________________________________________________________________________________
# SLINCING COM STRINGS: EX 1 
#print(frase[-3:])

#________________________________________________________________________________________________________________
# SLINCING COM STRINGS: EX 2
# Solicita ao usuário que digite seu endereço de e-mail e armazena na variável 'email'
#email = input('Digite seu endereço de email: ')

# Encontra a posição do caractere '@' na string 'email' e armazena em 'arroba'
#arroba = email.find('@')

# Imprime a posição do caractere '@' na string 'email'
#print(arroba)

# Extrai o nome de usuário (parte antes do '@') da string 'email' e armazena em 'usuario'
#usuario = email[0:arroba]

# Extrai o domínio (parte depois do '@') da string 'email' e armazena em 'dominio'
#dominio = email[arroba+1:]

# Imprime o nome de usuário
#print(usuario)

# Imprime o domínio
#print(dominio)


#________________________________________________________________________________________________________________
# FOR COM STRINGS
# produtos = 'carbonato de sódio e óxido de zinco'
# print('sódio' in produtos)
# print('magnésio' not in produtos)

#________________________________________________________________________________________________________________
# ENCONTRANDO ELEMENTOS NA STRING
# item = 'hipoclorito'
# pos = item.find('clor') # usando para encontrar um sub string dentro de outra ou um caractere
# print(pos)
# pos = item.find('flu') # retorna -1. Quando o método .find() retorna -1 significa que o valor não foi encontrado, e posso usar esse valor - 1 para fazer algum teste com if por exemplo.
# print(pos)

#________________________________________________________________________________________________________________

#TRANSFORMANDO PARA MAIÚSCULA:
objeto_celeste = 'galáxia esPiral M31'
print(objeto_celeste.upper())

#TRANSFORMANDO PARA MINÚSCULA:
objeto_celeste2 = 'galáxia esPiral M32'
print(objeto_celeste2.lower())

#________________________________________________________________________________________________________________
# SOMENTE A 1º LETRA DA FRASE TODA EM MAIÚSCULA:
objeto_celeste3 = 'galáxia esPiral M33'
print(objeto_celeste3.capitalize())

#________________________________________________________________________________________________________________
# COLOCA CADA LETRA DE CADA PALAVRA EM MAIÚSCULA:
objeto_celeste4 = 'galáxia esPiral M34'
print(objeto_celeste4.title())

#________________________________________________________________________________________________________________
# Substituindo um termo por outro. O método .replace() em Python é utilizado para substituir todas as ocorrências de um determinado termo por outro dentro de uma string.
suplemento = 'cloreto de magnésio'
novo_suplemento = suplemento.replace('magnésio', 'zinco') # 1º O que quero alterar, 2º O queremos colocar no lugar.
print(suplemento)
print(novo_suplemento)

#________________________________________________________________________________________________________________
# TRABALHANDO COM ESPAÇOS EM BRANCO:

frase = '    Ômega 3 é bom para a saude!    '
print(frase)
print(frase.lstrip()) #left - Remove os espaços a mais à esquerda da frase.
print(frase.rstrip()) # right - Remove os espaços a mais à direita da frase.
print(frase.strip()) # ambos- Remove tanto à esquerda quanto à direita ao memso tempo.

#________________________________________________________________________________________________________________
# ALINHAMENTOS DE STRING:
fruta = 'Abacate'
print(fruta)
print(fruta.rjust(20, '-')) # Usa 20 espaços para escrever a palavra Abacate e alinha a direita. *FOI COLOCADO '-' PARA PREENCHER OS ESPAÇOS
print(fruta.ljust(20, '-')) # Usa 20 espaços para escrever a palavra Abacate e alinha a esquerda. *FOI COLOCADO '-' PARA PREENCHER OS ESPAÇOS
print(fruta.center(20, '-')) # Centraliza a palavra Abacate. *FOI COLOCADO '-' PARA PREENCHER OS ESPAÇOS
# OBS: DA PARA USAR OS CARACTERES E O ALINAHMENTO PARA FAZER TÍTULOS OU MENUS.

#________________________________________________________________________________________________________________






