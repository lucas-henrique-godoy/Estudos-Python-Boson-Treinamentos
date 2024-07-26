# Dicionários: Permitem armazenar dados em pares chave valor. São similares à arrays associativos que existem em outras linguagens ou hach maps. Não permitem itens duplicados, masa os itens podem ser de qualquer tipo.
#  A chave é uma string que da acesso a um valor armazenado.
# Dentro do dicionário não  pode ter mais de 1 valor para a mesma chave, ou seja chaves repetidas, as chaves são imutáveis. Podemos usar string, valor numérico, ou até mesmo tuplas como chave, mas não itens que sejam mutáveis como as listas.
#  Podemos somente fazer alterações em um valor associado a uma chave, e não alterar a chave em si.
# - Se eu colocar o nome de uma chave que existe e atribuir um valor, o valor é alterado.
# - Se eu colocar o nome de uma chave que não exista e atribuir um valor, a chave será criada/ inserida nesse dicionário.

# CRIANDO UM DICIONÁRIO CHAMADO: ELEMENTO.
elemento = {
    'Z': 3,
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}

#________________________________________________________________________________________________________

# Acessando o dicionário:
print(f'Elemento: {elemento['nome']}.')
print(f'Densidade: {elemento['densidade']}.')

#________________________________________________________________________________________________________

# Verificando qual o tamanho do dicionário:
print(f'O dicionário possui: {len(elemento)} elementos.') # mostra a quantidade de pares chave valor

#________________________________________________________________________________________________________
# Atualizar uma entrada

# Mudando no dicionário o valor da chave 'grupo' de 'Metais Alcalinos' para 'Alcalinos'
#elemento['grupo'] = 'Alcalinos'
#print(elemento)
# - Se eu colocar o nome de uma chave que existe e atribuir um valor, o valor é alterado.


#________________________________________________________________________________________________________

# Adicionando uma entrada(criando uma nova chave) / Periodo foi criado
elemento['periodo'] = 1
print(elemento)
# - Se eu colocar o nome de uma chave que não exista e atribuir um valor, a chave será criada/ inserida nesse dicionário.

#________________________________________________________________________________________________________

# Exclusão de tens em dicionários / Periodo foi apagado
#del elemento['periodo']
#print(elemento)

#________________________________________________________________________________________________________

# Exclusão de todo o conteúdo do dicionário mas não do dicionário em si
#elemento.clear()
#print(elemento)

#________________________________________________________________________________________________________

# Exclusão do dicionário por completo
#del elemento
#print(elemento)

#________________________________________________________________________________________________________


# Retorna os itens do dicionário no formato dict_items. Na forma de uma lista de tuplas de pares chave valor. Possui colchetes indicando que todo o conteúdo é uma lista e  cada item esta dentro de uma tupla indicado por parenteses.
print(elemento.items())
for i in elemento.items():
    print(i)

#________________________________________________________________________________________________________
    # FORMAS DE MOSTRAR SOMENTE AS CHAVES DE UM DICIONÁRIO

print(elemento.keys()) # Mostra somente as chaves do dicionário dentro de uma dict_keys - Lista de tuplas.

for i in elemento.keys(): # Itera e mostra as chaves do dicionário uma em cima da outra.
    print(i)

#_____________________________________________________________________________________________________________
    # FORMAS DE MOSTRAR SOMENTE OS VALORES DE UM DICIONÁRIO

print(elemento.values())  # Mostra somente os valores do dicionário dentro de uma dict_values - Lista de tuplas.

for i in elemento.values(): # Itera e mostra os valores do dicionário um em cima do outro.
    print(i) 

#_______________________________________________________________________________________________________________

# Desempacotando as chaves valor simultaneamente.
# Retorna os itens como uma "tabela", "pequeno resumo", "pequeno relatório". Exemplo:
# Z: 3
# nome: Lítio
# grupo: Metais Alcalinos

for i, j in elemento.items(): # Iterando sobre os itens do dicionário(chave e valor). Onde i recebe a chave e o j recebe o valor.
    print(f'{i}: {j}')


