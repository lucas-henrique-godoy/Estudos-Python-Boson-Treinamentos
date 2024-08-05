# COMPREENSÃO DE LISTA: Uma técnica usada para aplicar uma funcionalidade em cima de elementos variados de uma sequencia ou de uma lista. Usada para criar e executar tarefas sobre listas.Permite que a gente derive uma lista nova a partir de outra lista, geralmente de forma concisa.

# SINTAXE GERAL: [expressão for item in lista]
# onde "expressão" é a expressão que será avaliada para cada elemento em "lista", e "item" é a variável de controle que representa cada elemento na lista, sequencialmente sobre a qual a expressao vai ser aplicada, retornando no final uma lista de itens.

# EXEMPLO 1- CRIAR UMA LISTA DE QUADRADOS A PARTIR DE OUTRA LISTA. USANDO COMPREENSÃO DE LISTA.
numeros = [1,4,7,9,10,12,21]

quadrados = [num**2 for num in numeros]
print(quadrados)

#_____________________________________________________________________________________________________________________

# EXEMPLO 2-  CRIAR UMA LISTA DE  NUMEROS PARES DE 0 A 10. USANDO COMPREENSÃO DE LISTA.
pares = [num for num in range(11) if num % 2 == 0] 
print(pares)

# OBS range é uma função que cria uma sequencia de valores numéricos

#_____________________________________________________________________________________________________________________

# EXEMPLO 3- CONTAR A QUANTIDADE DE VOGAIS DENTRO DE UM TEXTO. USANDO COMPREENSÃO DE LISTA.
frase = 'A lógica é apenas o princípio da sabedoria, e não o seu fim.'
vogais = ['a','e','i','o','u','á','é','í','ó','ú']

lista_vogais = [v for v in frase if v in vogais]
print(f'A frase possui {len(lista_vogais)} vogais: ')
print(lista_vogais)

#_____________________________________________________________________________________________________________________
#EXEMPLO 4- REALIZAR A MULTIPLICAÇÃO DOS ITENS DE UMA LISTA PELOS ITENS DE OUTRA LISTA. USANDO COMPREENSÃO DE LISTA.
# DISTRIBUTIVA ENTRE VALORES DE DUAS LISTAS.
distributiva = [k * m for k in [2,3,5] for m in [10,20,30]]
print(distributiva)

#OBS: É RECOMENDADO SE O CÓDIGO FICAR MUITO GRANDE OU COMPLEXO DIFICULTANDO A COMPREENSÃO, É MELHOR NÃO UTILIZAR A COMPRRENSAO DE LISTA SEGUNDO O PROFESSOR FÁBIO DA BÓSON TREINAMENTOS. NESSES CASOS É MELHOR UTILIZAR LAÇOS LAÇOS DE REPETIÇÃO CONVENCIONAIS.