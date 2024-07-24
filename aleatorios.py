# Números aleatótios inteiros

import random
import numpy as np

# Gerar números aleatórios - Um de cada vez dentro de um intervalo
valor = random.randint(1,20)
print(valor)
#_______________________________________________________________________________________________________________

print('Gerar cinco números aleatóris entre 1 e 50: \n')
for i in range(5):
    n = random.randint(1, 50)
    print(f'Número gerado: {n}')

#_______________________________________________________________________________________________________________

# Números aleatótios de ponto flutuante utilizando a função random.

valor = random.random()
print(f'Número gerado {round(valor * 10, 2)}') # Multiplica o valor da variável valor por 10 e arredonda o resultado para duas casas decimais.


#______________________________________________________________________________________________________________
# Números aleatótios de ponto flutuante utilizandoa função uniform.
valor = random.uniform(1,100)
print(f'Número: {round(valor, 4)}')

#______________________________________________________________________________________________________________
# Sortear um número a partir de uma lista 
lista = [2,4,6,9,10,13,14,16,18,20,21,27,33]
n = random.choice(lista)
print(f'Número escolhido: {n}')

#______________________________________________________________________________________________________________
# Sortear vários números a partir de uma lista
lista = [2,4,6,9,10,13,14,16,18,20,21,27,33]
n = random.sample(lista,3)
print(f'Número extraídos: {n}')

#______________________________________________________________________________________________________________

# Embaralhar aleatóriamente números de uma lista.
lista = [2,4,6,9,10,13,14,16,18,20,21,27,33]
print(f'Exibir a lista original: {lista}')
print(f'Embaralhar a lista e exibi-la:')
n = random.shuffle(lista)
print(lista)







        





