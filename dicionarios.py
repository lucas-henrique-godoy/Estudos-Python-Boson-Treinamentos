# Dicionários: Permitem armazenar dados em pares chave valor. São similares à arrays associativos que existem em outras linguagens ou hach maps. Não permitem itens duplicados, masa os itens podem ser de qualquer tipo.
#  A chave é uma string que da acesso a um valor armazenado.
# Dentro do dicionário não  pode ter mais de 1 valor para a mesma chave, ou seja chaves repetidas, as chaves são imutáveis. Podemos usar string, valor numérico, ou até mesmo tuplas como chave, mas não itens que sejam mutáveis como as listas. Podemos somente fazer alterações em um valor associado a uma chave, e não alterar a chave em si.
# - Se eu colocar o nome de uma chave que existe e atribuir um valor, o valor é alterado.
# - Se eu colocar o nome de uma chave que não exista e atribuir um valor, a chave será criada/ inserida nesse dicionário.


elemento = {
    'Z': 3,
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}

# Acessando o dicionário:
print(f'Elemento: {elemento['nome']}.')
print(f'Densidade: {elemento['densidade']}.')

# Verificando qual o tamanho do dicionário:
print(f'O dicionário possui: {len(elemento)} elementos.')

# Atualizar uma entrada
# 
# Mudando no dicionário o valor da chave 'grupo' de 'Metais Alcalinos' para 'Alcalinos'
#elemento['grupo'] = 'Alcalinos'
#print(elemento)

# Adicionando uma entrada(criando uma nova chave) / Periodo foi criado
#elemento['periodo'] = 1
#print(elemento)

# Exclusão de tens em dicionários / Periodo foi apagado
#del elemento['periodo']
#print(elemento)

# Exclusão de todo o conteúdo do dicionário mas não do dicionário em si
#elemento.clear()
#print(elemento)

# Exclusão do dicionário por completo
#del elemento
#print(elemento)


# Retorna os itens do dicionário no formato dict_items. Na foma de uma lista de tuplas. Possui colchetes indicando que todo o conteúdo é uma lista e  cada item esta dentro de uma tupla indicado por parenteses.
print(elemento.items())
for i in elemento.items():
    print(i)
