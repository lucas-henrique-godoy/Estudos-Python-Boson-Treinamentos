# Trocar valores entre duas variáveis:

var1 = 12
var2 = 31

var2, var1 = var1, var2
print(f'Var1: {var1}, Var2: {var2}')

#____________________________________________________________________________________________________________________

# Operador Condicional Ternário:

var1 = 12
var2 = 31

menor = var1 if var1 < var2 else var2
print(f'Menor valor: {menor}')
print(f'Menor valor: {(var2, var1)[var1 < var2]}')
#____________________________________________________________________________________________________________________

# Generators: Tipo especial de objeto parecido com compreensão de lista. Porém ele não retorna uma lista, mas sim um objeto especial iteravel do tipo generator. A grande vantagem do uso,  é que o conteudo gerado(lista de valores), não é gerador por completo na memória na hora, ao contrario das compreensões de lista que gera todo o conteudo na memoria de uma vez, se a lista for grande, pode consumir muitos recursos do sistema. O s generators nao consome recursos dessa forma, os valores não são gerados e guardados de uma vez na memoria, eles serao gerados e usados conforme forem solicitados, poupando recusos do meu sistema.

valores = [1,3,5,7,9,11,13,15]
quadrados = (item**2 for item in valores)
print(quadrados)
for valor in quadrados:
    print(valor)
#____________________________________________________________________________________________________________________

# Enumerate(): Função de iteração, permite iterar sobre elementos de uma sequencia qualquer(lista ou tupla), retornando os elementos e seus numeros de indice simultaneamente no formato de tuplas. É possivel acessar tanto os indices quanto os itens de forma separada ou em conjunto.

# ENUMERATE EXEMPLO 1:
bebidas = ['Café', 'Chá', 'Água', 'Suco', 'Refrigerante']
for i, item in enumerate(bebidas):
    print(f'Indice: {i}, Item: {item}')

# ENUMERATE EXEMPLO 2:
temperaturas = [-1,10,5,-3,8,4,-2,-5,7]
total = 0

for i, t in enumerate(temperaturas):
    if t < 0:
        print(f'A temperatura em {i} é negativa, com {t}°C.')
#____________________________________________________________________________________________________________________

# Gerenciamento de contexto com With: É uma forma simplificada para encapsular um bloco try except, com essa palavra With e associada a um esquema chamado de gerenciamento de contexto, que é algo que é programado dentro de determinadas classes, métodos e funções inclusive das que eu criar. Tendo como obejtivo simplificar códigos e torna-los menores para executar a mesma função e trazer ações de limpeza pré-definidas. Enbtão determinados códigos ficam programados dentro bloco with e são executados de forma independnete.




    
