# Declaração e inicialização de variáveis
media = 0
n1 = n2 = n3 = n4 = 0.0  # Todas as variáveis n1, n2, n3, n4 são inicializadas com o valor 0.0
nome, idade = 'Lucas', 47  # A variável nome recebe 'Lucas' e idade recebe 47
estado = True  # A variável estado recebe o valor booleano True

# Exemplos de utilização das funções type() e isinstance()

# Utilizando a função type() para verificar o tipo das variáveis
print(type(media))    # Saída: <class 'int'> (o tipo de media é int)
print(type(n2))       # Saída: <class 'float'> (o tipo de n2 é float)
print(type(nome))     # Saída: <class 'str'> (o tipo de nome é str)
print(type(estado))   # Saída: <class 'bool'> (o tipo de estado é bool)
print(type(1+2j))     # Saída: <class 'complex'> (o tipo de 1+2j é complex)

# Utilizando a função isinstance() para verificar se uma variável é de um determinado tipo
a = 10
b = 'Sol'
print(isinstance(a, (int, float)))  # Saída: True (a é do tipo int ou float)
print(isinstance(b, (int, float)))  # Saída: False (b não é do tipo int ou float)

# Execução de operações matemáticas simples
a = 40
c = 3
r = a * c  # Multiplicação de a por c, atribuindo o resultado a r
print(r)   # Saída: 120 (imprime o valor de r, que é 120)
