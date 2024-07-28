# FUNÇÕES: Bloco de cócdigo que executa uma determinada tarefa.
# Modularização: Possível tornar meu código modular, criando um bloco de códigos que realiza uma determinada função e usando posteriormente. Promovendo reuso de código. Melhora a legibilidade dos meus programas.

# Criandos Funções: SINTAXE: Obrigatório de toda função ter parenteses e dentro deles pode ou não haver argumento.
#  def <nome_função> ([argumentos]):
#        <instruções>

#EXEMPLO 1- Função sem argumentos: 
#def mensagem():
#    print('Bóson Treinamentos em Tecnologia')
#    print('Curso Completo de Python.')

# Chamando a função
#mensagem()

#_____________________________________________________________________________________________________________________
# EXEMPLO 2 - Função com argumentos mas sem `return`
# Neste exemplo, a função `soma` recebe dois argumentos e imprime o resultado da soma na tela.
# A função usa `print` para exibir o valor, mas **não retorna** esse valor.
# Isso significa que o valor calculado não pode ser armazenado em uma variável 
# ou utilizado para outros cálculos ou tarefas.
# OBS: A função abaixo não retorna o resultado; apenas o imprime. Isso significa que o valor da soma não é retornado para o programa e não pode ser usado fora da função.

#def soma(a, b):
#    print(a + b) # A função imprime o resultado da soma, mas não retorna o valor.

#soma(12, 7) # Chamando a função `soma` com os argumentos 12 e 7. O resultado da soma (19) será exibido na tela.

# Observação: Como a função não usa `return`, não é possível armazenar o resultado
# em uma variável ou usá-lo em cálculos adicionais. Para isso, a função deveria 
# retornar o valor

#_____________________________________________________________________________________________________________________
# EXEMPLO 3 - Função com Argumentos e `return`
# Neste exemplo, a função `mult` recebe dois argumentos e retorna o produto desses argumentos.
# A função usa `return` para devolver o resultado da multiplicação para o ambiente de execução.
# Isso permite que o valor calculado seja armazenado em uma variável e usado em outras partes do código.

#def mult(x, y):
#    return x * y # A função retorna o resultado da multiplicação dos argumentos `x` e `y`.

# Definindo as variáveis `a` e `b` com os valores 5 e 8, respectivamente.
#a = 5
#b = 8
#c = mult(a, b) # Chamando a função `mult` com os argumentos `a` e `b`, e armazenando o resultado na variável `c`.

#print(f'O produto de {a} e {b} é: {c}') # Exibindo o resultado da multiplicação. O valor de `c` (40) é impresso na tela.

# Observação: Como a função `mult` usa `return`, o valor calculado (o produto de `a` e `b`)
# é retornado e pode ser armazenado em uma variável (`c`) para uso posterior.
# OBS: Ao chamar a função, os nomes das variáveis usadas para fornecer os argumentos (neste caso `a` e `b`) não precisam ser os mesmos nomes dos parâmetros na definição da função (`x` e `y`).
# - O que importa é a ordem dos argumentos. Neste exemplo:
#   - O valor de `a` (5) é passado para `x`.
#   - O valor de `b` (8) é passado para `y`.

#_____________________________________________________________________________________________________________________

#EXEMPLO 4:
# Define a função `div` que realiza a divisão de `k` por `j`.
# def div(k, j):
#     # Verifica se o denominador `j` não é zero para evitar divisão por zero.
#     if j != 0:
#         # Se `j` não for zero, retorna o resultado da divisão `k / j`.
#         return k / j
#     else:
#         # Se `j` for zero, retorna uma mensagem de erro.
#         return 'Impossível dividir por zero!'

# # Verifica se o módulo está sendo executado diretamente.
# # Se o módulo for executado diretamente (não importado), `__name__` será igual a `'__main__'`.
# if __name__ == '__main__': 
#     # Solicita ao usuário que insira um número e converte a entrada para um inteiro.
#     a = int(input('Digite um número: '))
#     # Solicita ao usuário que insira outro número e converte a entrada para um inteiro.
#     b = int(input('Digite outro número: '))

#     # Chama a função `div` com os números fornecidos pelo usuário e armazena o resultado em `r`.
#     r = div(a, b)
    
#     # Imprime o resultado da divisão ou a mensagem de erro, dependendo do valor de `b`.
#     print(f'{a} dividido por {b} é igual a {r}')


#OBS: if __name__ == '__main__': Usado para separar a area de criação das funções da área que efetivamente vai executar o código. Indica o ponto principal de entrada no programa e separa isso organizando melhor o código.
#_____________________________________________________________________________________________________________________

# EXEMPLO 5 - Função para calcular valores de quadrados:

# Define a função `quadrado` que recebe uma lista de valores e retorna uma lista com os quadrados desses valores.
def quadrado(val):
    # Cria uma lista vazia para armazenar os quadrados dos valores.
    quadrados = []
    
    # Itera sobre cada valor na lista `val`.
    for x in val:
        # Adiciona o quadrado do valor `x` à lista `quadrados`.
        quadrados.append(x ** 2)
    
    # Retorna a lista `quadrados` com os valores quadrados.
    return quadrados

# Verifica se o módulo está sendo executado diretamente.
# Se o módulo for executado diretamente (não importado), `__name__` será igual a `'__main__'`.
if __name__ == '__main__':
    # Define uma lista de valores.
    valores = [2, 5, 7, 9, 12]
    
    # Chama a função `quadrado` com a lista `valores` e armazena o resultado na variável `resultados`.
    resultados = quadrado(valores)
    
    # Itera sobre cada valor na lista `resultados`.
    for g in resultados:
        # Imprime o valor de cada elemento na lista `resultados`, que são os quadrados dos valores originais.
        print(g)

    

