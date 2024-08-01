#               FUNÇÕES LAMBDA (anônimas) :

#  Funções que não tem nome, e que podem ser criadas e usadas no mesmo momento. A gente não define uma função previamente para usar depois, você cria e usa na mesma hora a funçã lambda. Trata-se de uma expressão única numa instrução e ela pode ser empregada em lugares no código onde nós não conseguiriamos usar uma função def comum, por ecemplo dentro de uma lista u até mesmo dentro da chamada de outra função. É como se fosse uma espécie de um atalho de função. As funções lambdas podem simplificar alguns cenários de codificação, por exemplo quando queremos executar funçoes que são simples dentro de algum trecho de código.
# Sintaxe:
# lambda argumentos: expressão

# EX1 - FUNÇÃO LAMBDA QUE RETORNE O QUADRADO DE UM NÚMERO
# quadrado = lambda x: x**2 

# for i in range(1,11):
#     print(quadrado(i))


# EX2 - FUNÇÃO LAMBDA PARA VERIFICAR SE UM NÚMERO É PAR

# par = lambda x: x % 2 == 0
# print(par(27))


# EX3 - FUNÇÃO LAMBDA PARA CONVERTER TEMPERATURA DE GRAUS FAREHEINT PARA CELSIUS

# f_c = lambda f: (f - 32) * 5/9
# print(f_c(32))
#_________________________________________________________________________________________________________________________

#               FUNÇÃO MAP()

# Sintaxe: # map(função, iterável) 
# Cada função que for passada sera aplicada para cada item dentro desse objeto iterável. Ex: Lista, tupla, dicionário. Pode ser uma função normal def ou lambda.
# OBS: O iterável é o obejto que vai receber essa função.

#EXEMPLO 1 : FUNÇÃO DE DOBRAR OS ITENS DE UMA LISTA USANDO MAP E LAMBDA.
num = [1,2,3,4,5,6,7,8]
dobro = list(map(lambda x: x * 2, num))
print(dobro)

#EXEMPLO 2 : FUNÇÃO PARA CONVERTER AS STRINGS PARA MAIÚSCULAS.
palavras = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']
maiúsculas = list(map(str.upper, palavras))
print(maiúsculas)
#_________________________________________________________________________________________________________________________

# A idéia da função lambda e map, são idéas que vem da programação funcional, que é um paradigma distinto da procedural, orientada a objetos. python tem suporte à programação funcional, por isso possui essas funções disponíveis.

# A função map especificamente é uma função que é chamada em programação funcional, de função de ordem superior. que é uma função que pode receber outras funções como argumento, e/ou retornar outras funções como resultado.
#_________________________________________________________________________________________________________________________

# FUNÇÃO FILTER()



