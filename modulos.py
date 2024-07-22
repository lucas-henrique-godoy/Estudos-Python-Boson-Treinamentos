#EXEMPLOS DE COMO IMPORTAR MÓDULOS EM PYTHON

# EX1 - import math -> Importação simples de um módulo

# EX2 - from math import sqrt, sin ->  Importar Funções e Variáveis Específicas

# EX3 - from math import * -> Import universal: Importa todas as funções de um módulo, não é muito recomendado, pois pode gerar conflitos om outros pacotes que podem possuir os mesmos nomes de algum constituinte dessa biblioteca. Usar com cautela.

# EX4 -  import math as m -> Utilizando apelidos.
# print(m.sqrt(81))

import mod_func as mf # Importa o módulo mod_func e usa o alias mf para se referir a ele
import numpy as np # Importa o módulo numpy e usa o alias np para se referir a ele

if __name__ == '__main__': # O código abaixo será executado somente se este script for o ponto de entrada principal
     mf.mensagem() # Chama a função mensagem() do módulo mod_func, se ela estiver definida

     num = int(input(' Digite um número inteiro positivo: ')) # Solicita ao usuário um número inteiro positivo

     print(f'\nCalcular fatorial do número: ') # Calcula o fatorial do número digitado
     fat = mf.fatorial(num) # Chama a função fatorial() do módulo mod_func, passando num como argumento
     print(f'O fatorial é: {fat}') # Exibe o resultado do cálculo do fatorial

     # Calcula a sequência de Fibonacci até o número digitado   
     print(f'\nCalcular sequência de fibonacci: ')
     fib = mf.fibonacci(num) # Chama a função fibonacci() do módulo mod_func, passando num como argumento
     print(f'A sequência de fibonacci é: {fib}') # Exibe a sequência de Fibonacci calculada
    

#_________________________________________________________________________________________________________________

# Utilizando uma funcionalidade do módulo numpy
L = np.array([1,2,3,4,5,6,7,8,9]) #cria uma matriz unidimensional utilizando a biblioteca NumPy com apelido definido por mim como np em Python.
print(L) # Mostra a matriz unidimensional






