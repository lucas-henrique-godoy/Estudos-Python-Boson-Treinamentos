# Inicialização das variáveis x, y e z como False
x = y = z = False

# Inicialização das variáveis n1 e n2 como 0
n1 = n2 = 0

# Solicitação e leitura do primeiro número digitado pelo usuário
print('Digite um número: ')
n1 = int(input())

# Solicitação e leitura do segundo número digitado pelo usuário
n2 = int(input('Digite outro número: '))

# Verifica se n1 é igual a n2 e atribui o resultado a variável x
x = n1 == n2
# Imprime se os números são iguais e o valor de x
print('São iguais?:', x, '\n')

# Verifica se n1 é maior que n2 e atribui o resultado a variável z
z = n1 > n2
# Imprime se n1 é maior que n2 e o valor de z
print(n1, ' é maior que ', n2, '?', z, '\n')

# Verifica se n1 é diferente de n2 e atribui o resultado a variável y
y = n1 != n2
# Imprime se os números são diferentes e o valor de y
print('São diferentes? ' + str(y))
