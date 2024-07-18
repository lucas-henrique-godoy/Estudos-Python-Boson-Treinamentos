# Simples, Composto, Encadeado.

n1 = n2 = 0.0
media = 0.0

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

# Calcula a média aritmética das notas
media = (n1 + n2) / 2

if (media >= 7):
    print('Resultado: Aprovado!')
    print('Parabéns!')
else:
    print('Resultado: Reprovado!')
    print('Você precisa estudar mais!')

print('Sua média é {}' . format(media))