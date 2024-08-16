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

# Generators
