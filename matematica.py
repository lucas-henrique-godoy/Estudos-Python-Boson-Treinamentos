import math

# Funções builtin (internas)

valores = [2,5,8,-1,0,11,7,-6]
print(max(valores))   # VALOR MÁXIMO
print(min(valores))   # VALOR MÍNIMO

a = -5
b = 4
print(abs(a))     # NÚMERO ABSOLUTO
print(pow(a, b))  # POTENCIAÇÃO
c = 2.789011
print(round(c, 3))    # Arredonda e formata as casas decimais. 1º Pede qual valor a ser arredondado (neste caso: variavel c). 2º Pede numero de  casas decimais que eu quero utilizar.

#___________________________________________________________________________________________________________________________________________________________________________________

# Funções do módulo math
x = 8
y = 100

        # RAIZ QUADRADA
 
raiz_quadrada = math.sqrt(x) # Mostra a raiz quadrada de um valor.
print(math.ceil(raiz_quadrada)) # arredonda para cima para o inteiro mais próximo.

raiz_quadrada = math.sqrt(x)
print(math.floor(raiz_quadrada)) # arredonda para baixo para o inteiro mais próximo.

print(round(raiz_quadrada, 2)) # Arredonda e formata as casas decimais.

#___________________________________________________________________________________________________________________________________________________________________________________
        # LOGARITMO: Valor ao qual eu vou elevar um valor, para chegar a outro valor.        
logaritmo = math.log10(y)
print(logaritmo)

#___________________________________________________________________________________________________________________________________________________________________________________
# CONSTANTE PI:
print(math.pi)

#___________________________________________________________________________________________________________________________________________________________________________________

# FATORIAL:
print(math.factorial(x))

#___________________________________________________________________________________________________________________________________________________________________________________
# INFINITO:
print(x / math.inf)



