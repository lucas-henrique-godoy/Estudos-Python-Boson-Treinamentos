# EXEMPLO 1:
lista = [2, 6, 9, 4, 0, 12, 3, 7]

# Percorre cada elemento da lista e imprime cada item
for item in lista:
    print(item)

#___________________________________________________________________________________________________________

# EXEMPLO 2:
palavra = 'Lucas'

# Percorre cada caractere da string 'Lucas' e imprime cada letra
for letra in palavra:
    print(letra)

#___________________________________________________________________________________________________________

# EXEMPLO 3:
# Utiliza range para gerar números de 1 a 10 (valor_final é exclusivo) e os imprime
for numero in range(1, 11):
    print(numero)

#___________________________________________________________________________________________________________

# EXEMPLO 4:
# Usa range para gerar números de 0 a 9 (valor_final é exclusivo) e os imprime
for numero in range(10):
    print(numero)

#___________________________________________________________________________________________________________

# EXEMPLO 5:
nome = input('Digite seu nome: ')

# Imprime o nome do usuário 10 vezes, prefixando cada linha com o número da iteração (de 1 a 10)
for x in range(10):
    print(f'{x + 1} {nome}')

#___________________________________________________________________________________________________________

# SINTAXE: range(valor_inicial, valor_final, incremento)

#___________________________________________________________________________________________________________

# EXEMPLO 6:
# Usa range com um incremento negativo (-2), começando em 20 e terminando em 4 (pois valor_final é exclusivo)
for x in range(20, 2, -2):
    print(x)

#___________________________________________________________________________________________________________

# EXEMPLO 7:
pedras = ('Rubi', 'Esmeralda', 'Quartzo', 'Safira', 'Diamante', 'Turmalina')

# Itera sobre a tupla 'pedras' e imprime cada pedra, exceto 'Quartzo', utilizando 'continue' para pular esta iteração
for pedra in pedras:
    if pedra == 'Quartzo':
        continue
    print(pedra)
