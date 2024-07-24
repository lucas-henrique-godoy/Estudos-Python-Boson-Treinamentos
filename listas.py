#     EXEMPLOS DE MANIERAS DE TRABALHAR COM LISTAS
# Lista: representa uma sequência de valores
# Sintaxe: nome_lista = [valores]

# Definição das listas n1 e n2
#n1 = [4, 6, 7, 8, 0, 3]
#n2 = [1, 6, 3, 0, 12, 11]
#___________________________________________________________________________________________________________

# Concatenação das listas n1 e n2
#valores = n1 + n2
#___________________________________________________________________________________________________________

# Imprime a lista completa
# print(valores)
#___________________________________________________________________________________________________________

# Imprime o tipo da variável (deve ser list)
# print(type(valores))
#___________________________________________________________________________________________________________

# Acessa e imprime o último valor da lista
# print(valores[-1])
#___________________________________________________________________________________________________________

# Acessa e imprime o penúltimo valor da lista
# print(valores[-2])
#___________________________________________________________________________________________________________

# Modifica o primeiro elemento da lista para o valor 9
# valores[0] = 9  
#___________________________________________________________________________________________________________

# Imprime o tamanho da lista valores (quantidade de elementos)
# print(len(valores))
#___________________________________________________________________________________________________________

# Imprime a lista valores ordenada em ordem crescente
# print(sorted(valores))
#___________________________________________________________________________________________________________

# Imprime a lista valores ordenada em ordem decrescente
# print(sorted(valores, reverse=True))
#___________________________________________________________________________________________________________

# Calcula e imprime a soma de todos os elementos da lista valores
# print(sum(valores))
#___________________________________________________________________________________________________________

# Encontra e imprime o valor mínimo na lista valores
# print(min(valores))
#___________________________________________________________________________________________________________

# Encontra e imprime o valor máximo na lista valores
# print(max(valores))
#___________________________________________________________________________________________________________

# Imprime os dois primeiros elementos da lista
# print(valores[0:2])
#___________________________________________________________________________________________________________

# Imprime os quatro primeiros elementos da lista
# print(valores[:4])
#___________________________________________________________________________________________________________

# Imprime os elementos a partir do índice 3 até o final da lista
# print(valores[3:])
#___________________________________________________________________________________________________________

# Imprime uma lista vazia (pois os índices são iguais, portanto não há elementos)
# print(valores[3:3])
#___________________________________________________________________________________________________________

# Imprime os dois últimos elementos da lista
# print(valores[-2:])
#___________________________________________________________________________________________________________

##valores.append(13) # adiciona um valor na ultima posição
##print(valores)
##valores.pop() # remove um valor da ultima posição
##print(valores)
##valores.pop(3) # remove um valor na posição expecificada (posição 3)
##print(valores)
##valores.insert(3,21) # insere um valor e empurra os demais para posições posteriores (1º parametro - posição, 2ºparametro-valor a ser inserido)
##print(valores)
##print(12 in valores) # verifica se o valor 12 esta presente na lista e retorna um booleano como resposta
##print(valores.index(12)) # mostra qual a posição o valor 12 ocupa na lista.

# OBS: A atribuição (lista[indice] = valor) substitui o valor em uma posição específica da lista sem alterar a posição dos demais elementos. Já o método insert() insere um novo valor em uma posição específica da lista e desloca os elementos subsequentes para posições posteriores.

#___________________________________________________________________________________________________________

#EXEMPLO 2
# HÁ FORMAS DE CRIAR LISTAS VAZIAS E DEPOIS PODEMOS PREENCHE-LAS USANDO O método .apeend():
# planetas = [] OU
# planetas = list()

#___________________________________________________________________________________________________________
#EXEMPLO 3
# planetas = ['Mercúrio', 'Vênus', 'Marte', 'Saturno', 'Urano', 'Netuno']
# for planeta in planetas:
#     print(planeta)

#___________________________________________________________________________________________________________

# EXERCICIO:  Crie um script que peça para o usuário digitar o nome de 5 bebidas favoritas dele, armazenando esses valores em uma lista.
# Na sequência, exiba na tela os elementos da lista em ordem alfabética, um por linha, usando um laço de repetição for.

bebidas = []  # Inicializa uma lista vazia para armazenar as bebidas

# Loop para iterar 5 vezes
for i in range(5):
    print(f'Digite uma bebida favorita: ')  # Solicita ao usuário que digite o nome de uma bebida
    bebida = input()  # Captura a entrada do usuário (nome da bebida) e armazena na variável bebida
    bebidas.append(bebida)  # Adiciona a bebida digitada à lista bebidas

bebidas.sort()  # Ordena a lista bebidas em ordem alfabética

print(f'\nBebidas escolhidas: ')
for bebida in bebidas:
    print(bebida)  # Imprime cada bebida da lista ordenada, uma por linha

print(f'\nSaúde!')  # Exibe uma mensagem de encerramento após exibir todas as bebidas


    