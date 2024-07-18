#  Condicionais Simples, Composto, Encadeado.

# Inicialização das variáveis
n1 = n2 = 0.0
media = 0.0

# Solicita ao usuário que digite as notas
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

# Calcula a média aritmética das notas
media = (n1 + n2) / 2

# Condição simples: verifica se a média é maior ou igual a 7
if media >= 7:
    print('Resultado: Aprovado!')
    print('Parabéns!')
# Condição composta: verifica se a média é menor que 7 e maior ou igual a 5
elif media >= 5:
    print('Você está de recuperação!')
# Caso contrário, executa o bloco do else
else:
    print('Aluno reprovado...')

# Imprime a média calculada
print('Sua média é {}' . format(media))
