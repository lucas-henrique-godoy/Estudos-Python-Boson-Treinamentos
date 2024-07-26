# SET: Conjuntos/coleções não ordenadas de valores únicos usados para armazenar múltiplos itens dentro de um objeto.
# - Apenas armazenam itens não duplicados, ou seja, não permitem que dois itens tenham o mesmo valor. Sets suportam operações matemáticas sobre conjuntos, como União, Interseção, Diferença e Diferença Simétrica.
# - Embora não seja possível modificar os itens existentes dentro de um set (os elementos devem ser imutáveis), é possível adicionar e remover elementos. Portanto, o set em si é mutável.
# - É possível armazenar elementos de diferentes tipos dentro de um set, desde que os elementos sejam imutáveis (por exemplo, números, strings e tuplas). Diferente dos dicionários, que possuem pares de chave-valor, o set contém apenas valores.
# - Quando acessamos um conjunto, oselementos vem em ordem aleatória.


# CRIANDO UM SET:
# planeta_anao = {'Plutão', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
# print(planeta_anao)

# # Verificando quantos itens tem dentro do set:
# print(len(planeta_anao))

# # Verificar se ha um valor expecífico dentro do set:
# print('Ceres' in planeta_anao) # Retorna a resposta em um booleano (Ceres está dentro de planeta_anao?)

# # Verfica se não há um valor expecífico dentro do set:
# print('Lua' not in planeta_anao) # Retorna a resposta em um booleano (LUA NÃO ESTA DENTRO DE planeta_anao?)


# # Iteração sobre o set(conjunto):
# for astro in planeta_anao:
#     print(astro.upper())

#________________________________________________________________________________________________________________________
# CRIANDO CONJUNTOS A PARTIR DE OUTRAS SEQUÊNCIA:

# TRANSFORMANDO UMA LISTA EM UM SET:

# astros = ['Lua', 'Vênus', 'Sirius', 'Marte', 'Lua']  # Lista usada para criar um set a partir dela.
# print(astros, end=' ')  # Imprime a lista original com duplicatas. Aqui, 'Lua' aparece duas vezes.
# astro_set = set(astros)  # Transforma a lista 'astros' em um set 'astro_set', removendo duplicatas.
# print(astro_set)  # Imprime o set resultante. 'Lua' aparece apenas uma vez, pois sets não permitem duplicatas.

#_________________________________________________________________________________________________________________________________________________________________________
# FAZENDO COMPARAÇÕES ENTRE SETS/CONJUNTOS:

astros1 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Io'}
astros2 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Cometa de Halley'}

# Comparações entre os conjuntos
# print(astros1 == astros2)  # RETORNO - False: astros1 e astros2 não são iguais porque 'astros2' contém um elemento a mais.
# print(astros1 > astros2)   # RETORNO - False: astros1 não é um conjunto estritamente maior que astros2 (astros1 não contém todos os elementos de astros2).
# print(astros1 >= astros2)  # RETORNO - False: astros1 não é um conjunto que contém todos os elementos de astros2 (astros1 não é um superset de astros2).
# print(astros1 < astros2)   # RETORNO - True: astros1 é um conjunto estritamente menor que astros2 (todos os elementos de astros1 estão em astros2, mas astros2 tem elementos adicionais).
# print(astros1 <= astros2)  # RETORNO - True: astros1 é um subconjunto de astros2 (todos os elementos de astros1 estão em astros2).
# print(astros1 != astros2)  # RETORNO - True: astros1 e astros2 são diferentes devido ao elemento adicional em astros2.

#_________________________________________________________________________________________________________________________________________________________________________
# UNIÃO DE CONJUNTOS

# PRIMEIRA MANEIRA DE UNIR CONJUNTOS/SET:
# print(astros1 | astros2)  # Une os conjuntos 'astros1' e 'astros2', resultando em um novo conjunto com todos os elementos únicos dos dois conjuntos.

# SEGUNDA MANEIRA DE UNIR CONJUNTOS/SET:
# print(astros1.union(astros2))

#_________________________________________________________________________________________________________________________________________________________________________
# INTERSECÇÃO DE CONJUNTOS/SET: CONJUNTO QUE TEM APENAS OS ELEMENTOS EM COMUM, OU SEJA QUE ESTÃO EM AMBOS OS CONJUNTOS:

# PRIMEIRA MANEIRA DE FAZER UMA INTERSECÇÃO DE CONJUNTOS/SET:
#print(astros1 & astros2)

# SEGUNDA MANEIRA DE FAZER UMA INTERSECÇÃO DE CONJUNTOS/SET:
#print(astros1.intersection(astros2))

#_________________________________________________________________________________________________________________________________________________________________________
# DIFERENÇA SIMÉTRICA DE CONJUNTOS/SET: RETORNA OS ELEMENTOS QUE NÃO APARECEM EM AMBOS OS CONJUNTOS.

# PRIMEIA MANEIRA DE ENCONTRAR A DIFERENÇA SIMÉTRICA:
#print(astros1 ^ astros2) # retorna os unicos elementos que não aparecem nos 2 conjuntos.

# PRIMEIA MANEIRA DE ENCONTRAR A DIFERENÇA SIMÉTRICA: 
#print(astros1.symmetric_difference(astros2)) # retorna os unicos elementos que não aparecem nos 2 conjuntos

#_________________________________________________________________________________________________________________________________________________________________________

# ACRESCENTANDO ELEMENTOS EM UM CONJUNTO:

astros1.add('Urano')
astros1.add('Sol')

#_________________________________________________________________________________________________________________________________________________________________________

# REMOVENDO ELEMENTOS EM UM CONJUNTO:
# PRIMEIRA MANEIRA DE REMOVER
astros1.remove('Io') # REMOVENDO O ELEMENTO 'Io'

#_________________________________________________________________________________________________________________________________________________________________________

#SEGUNDA MANEIRA DE REMOVER:
#astros1.discard('Plutão') # Esse método não retorna keyError caso você tente remover um item que não existe dentro do conjunto
#_________________________________________________________________________________________________________________________________________________________________________

print(astros1) # MOSTRA O CONJUNTO 'astros1' DEPOIS DO ITEM 'IO' SER REMOVIDO. RETORNO: {'Urano', 'Sol', 'Lua', 'Marte', 'Vênus', 'Sirius'}
#print(sorted(astros1))

#_________________________________________________________________________________________________________________________________________________________________________
# OBS: SE TENTAR REMOVER UM ITEM QUE NÃO EXISTE NO CONJUNTO ESPECIFICADO OBTEMOS UM ERRO DE CHAVE COMO RETORNO: KeyError.
#EX: 
#astros1.remove('Plutão') # ERRO DE RETORNO: KeyError: 'Plutão'
#print(astros1)
#_________________________________________________________________________________________________________________________________________________________________________

astros1.discard('Plutão') # Esse método não retorna keyError caso você tente remover um item que não existe dentro do conjunto.
print(astros1)

#_________________________________________________________________________________________________________________________________________________________________________

#REMOVER O ELEMENTO ARBITRÁRIO:
astros1.pop() # remove itens de forma aleatória **OBS: pode ser usado em aplicações como jogos por exemplo.

#_________________________________________________________________________________________________________________________________________________________________________
# LIMPAR TOTALMENTE O CONJUNTO:
astros1.clear() # retorna: set() indicando que nao ha mais nada dentro do conjunto.
print(astros1)



