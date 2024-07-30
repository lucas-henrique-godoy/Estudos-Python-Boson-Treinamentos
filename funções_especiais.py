# Funções lambda (anônimas) - Funções que não tem nome, e que podem ser criadas e usadas no mesmo momento. A gente não define uma função previamente para usar depois, você cria e usa na mesma hora a funçã lambda. Trata-se de uma expressão única numa instrução e ela pode ser empregada em lugares no código onde nós não conseguiriamos usar uma função def comum, por ecemplo dentro de uma lista u até mesmo dentro da chamada de outra função. É como se fosse uma espécie de um atalho de função. As funções lambdas podem simplificar alguns cenários de codificação, por exemplo quando queremos executar funçoes que são simples dentro de algum trecho de código.
# Sintaxe:
# lambda argumentos: expressão

# EX1 - FUNÇÃO LAMBDA QUE RETORNE O QUADRADO DE UM NÚMERO
# quadrado = lambda x: x**2 

# for i in range(1,11):
#     print(quadrado(i))

#_________________________________________________________________________________________________________________________

# EX2 - FUNÇÃO LAMBDA PARA VERIFICAR SE UM NÚMERO É PAR

# par = lambda x: x % 2 == 0
# print(par(27))

#_________________________________________________________________________________________________________________________

# EX3 - FUNÇÃO LAMBDA PARA CONVERTER TEMPERATURA DE GRAUS FAREHEINT PARA CELSIUS

# f_c = lambda f: (f - 32) * 5/9
# print(f_c(32))
#_________________________________________________________________________________________________________________________

# FUNÇÃO MAP().
                      