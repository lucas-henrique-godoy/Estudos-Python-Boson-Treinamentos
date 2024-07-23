# Lista: representa um sequência de valores

# Sintaxe: nome_lista = [valores]

# notas = [5,7,8,6,9]
# print(notas)

n1 = [4,6,7,8,0,3]
n2 = [1,6,3,0,12,11]
valores = n1 + n2
# print(valores)
# print(type(valores))
# print(valores[-1]) -> acessa o ultimo valor da lista
# print(valores[-2]) -> acessa o penultimo valor da lista
valores[0] = 9
# print(valores[0:2])
# print(valores[:4])
print(valores[3:4])