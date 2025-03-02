# TUPLAS: SÃO IMUTÁVEIS. NÃO É POSSÍVEL ALTERAR CONTEÚDO DA TUPLA DEPOIS DA TUPLA TER SIDO CRIADA. PODEM CONTER QUAISQUER TIPOS DE DADOS

# EXEMPLO DE TUPLA:
tupla = (2,4,6,7,9)
tupla[0] = 1    # Não é possivel modificar ou atribuir novos valores a uma tupla depois de ela ja ter sido criada.
print(tupla)
print(tupla[-1]) # Acessa o ultimo valor da tupla
#____________________________________________________________________________________________________________

halogenios = ('F', 'Cl', 'Br', 'I', 'At') # 1º TUPLA
print(halogenios[3]) # Acessando um elemento
print(len(halogenios)) # mostra quantos elemntos existem dentro da tupla

# 2º TUPLA
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres # Concatenação de tuplas. Junta as 2 tuplas em uma e atribui a tupla resultante na variavel elementod
t1 = (5,2,6,8,4,5,6,4,4,0,12,22,3,4,5)
print(halogenios[-2:])
print('Fe' in halogenios) # Verifica se 'Fe' esta dentro da tupla e retorna um booleano. Neste caso um False
print(sum(t1)) # Soma os elementos da tupla
print(min(t1)) # retorna o valor minimo que esta dentro da tupla
print(max(t1)) # retorna o valor máximo que esta dentro da tupla.


# Operações não disponíveis em tuplas: .sort(), .append(), .reverse(), .pop()... Ou seja todos os métodos que alteram o conteúdo da tupla não estão disponíveis. 

#_____________________________________________________________________________________________________________________________________________________________

# ITERAÇÃO EM TUPLAS
for elemento in elementos:
    print(f'Elemento químico: {elemento}')

#_____________________________________________________________________________________________________________________________________________________________

# criando uma lista a partir de uma tupla:

grupo17 = list(halogenios) # transforma a tupla em uma lista, permitindo modificações
grupo17[0] = 'H' # modifica um item da lista, não da tupla
print(grupo17)  # Exibe a lista modificada
print(type(grupo17)) # verifica o tipo do objeto
#_____________________________________________________________________________________________________________________________________________________________

# criando uma tupla a partir de uma lista:

grupo1 = ['Li', 'Na', 'K','Rb', 'Cs', 'Fr']
alcalinos = tuple(grupo1) # transforma a tupla em uma lista
print(alcalinos) # exibe a tupla
print(type(alcalinos)) # verifica o tipo do objeto

#_____________________________________________________________________________________________________________________________________________________________

# Não é possível reordenar os elementos dentro de uma tupla, porém é possível criar uma nova tupla com os elementos de uma tupla classificados.

print(sorted(alcalinos)) # Ordena os elementos e retorna uma nova lista em ordem crescente ou alfabética.
print(alcalinos.sort())  # Esse método de ordenação não funciona em tuplas pois modifica seus elementos.

#  OBS: sorted() é uma função que cria uma nova lista ordenada a partir de qualquer objeto iterável, sem modificar o original.

# .sort() é um método de lista que ordena a lista original in-place, ou seja, modifica a lista diretamente.
# A falta de .sort() em tuplas (e outras estruturas imutáveis) decorre da natureza imutável dessas estruturas em Python.
