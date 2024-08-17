# Trocar valores entre duas variáveis:

var1 = 12
var2 = 31

# Troca os valores das variáveis usando uma atribuição simultânea
var2, var1 = var1, var2
print(f'Var1: {var1}, Var2: {var2}')  # Exibe os valores trocados

#____________________________________________________________________________________________________________________

# Operador Condicional Ternário:

var1 = 12
var2 = 31

# Usa o operador condicional ternário para atribuir o menor valor entre var1 e var2 à variável 'menor'
menor = var1 if var1 < var2 else var2
print(f'Menor valor: {menor}')  # Exibe o menor valor

# Alternativamente, usa uma expressão de tupla para obter o menor valor
print(f'Menor valor: {(var2, var1)[var1 < var2]}')  # Exibe o menor valor usando uma expressão de tupla
#____________________________________________________________________________________________________________________

# Generators: Tipo especial de objeto parecido com compreensão de lista. Porém ele não retorna uma lista, mas sim um objeto especial iteravel do tipo generator. A grande vantagem do uso,  é que o conteudo gerado(lista de valores), não é gerador por completo na memória na hora, ao contrario das compreensões de lista que gera todo o conteudo na memoria de uma vez, se a lista for grande, pode consumir muitos recursos do sistema. O s generators nao consome recursos dessa forma, os valores não são gerados e guardados de uma vez na memoria, eles serao gerados e usados conforme forem solicitados, poupando recusos do meu sistema.

valores = [1, 3, 5, 7, 9, 11, 13, 15]

# Cria um generator expression que calcula o quadrado de cada item em 'valores'
quadrados = (item**2 for item in valores)

# Exibe o objeto generator (será mostrado o tipo do generator, não o conteúdo)
print(quadrados)

# Itera sobre o generator e imprime cada valor gerado
for valor in quadrados:
    print(valor)
#____________________________________________________________________________________________________________________

# Enumerate(): Função de iteração, permite iterar sobre elementos de uma sequencia qualquer(lista ou tupla), retornando os elementos e seus numeros de indice simultaneamente no formato de tuplas. É possivel acessar tanto os indices quanto os itens de forma separada ou em conjunto.

# Exemplo 1: Usando enumerate para iterar sobre uma lista de bebidas
bebidas = ['Café', 'Chá', 'Água', 'Suco', 'Refrigerante']
for i, item in enumerate(bebidas):
    # Exibe o índice e o item da lista
    print(f'Indice: {i}, Item: {item}')

# Exemplo 2: Usando enumerate para iterar sobre uma lista de temperaturas
temperaturas = [-1, 10, 5, -3, 8, 4, -2, -5, 7]
for i, t in enumerate(temperaturas):
    if t < 0:
        # Exibe a posição e o valor das temperaturas negativas
        print(f'A temperatura em {i} é negativa, com {t}°C.')
#____________________________________________________________________________________________________________________

# Gerenciamento de contexto com With: É uma forma simplificada para encapsular um bloco try except, com essa palavra With e associada a um esquema chamado de gerenciamento de contexto, que é algo que é programado dentro de determinadas classes, métodos e funções inclusive das que eu criar. Tendo como obejtivo simplificar códigos e torna-los menores para executar a mesma função e trazer ações de limpeza pré-definidas. Então determinados códigos ficam programados dentro bloco with e são executados de forma independente.

# Gerenciamento de Contexto com `with`:
# Abre e lê um arquivo usando a palavra-chave 'with', que garante o fechamento automático do arquivo
# Usando 'try-except-finally' manualmente para comparação:
try:
    a = open('frutas.dat', 'r', encoding='utf-8')
    # Lê e imprime o conteúdo do arquivo
    print(a.read())
except IOError:
    # Exibe uma mensagem de erro se o arquivo não puder ser aberto
    print(f'Não foi possível abrir o arquivo!')
else:
    # Fecha o arquivo se não houve exceção
    a.close()

# Forma alternativa com 'with':
# O bloco 'with' garante que o arquivo será fechado automaticamente após o término do bloco
with open('frutas.dat', 'r', encoding='utf-8') as a:
    # Itera sobre cada linha do arquivo e imprime
    for linha in a:
        print(linha, end='')




    
