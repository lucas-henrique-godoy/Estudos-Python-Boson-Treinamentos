# Exeção é um objeto que representa um erro que ocorreu ao executar o programa.
# Blocos try ... except

# Solicita ao usuário que digite dois números inteiros
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

try:
    # Dentro do bloco 'try' coloca-se o código que pode gerar uma exceção
    # Aqui, estamos tentando dividir n1 por n2 e arredondar o resultado para duas casas decimais
    # Se n2 for zero, isso gerará uma exceção ZeroDivisionError
    r = round(n1 / n2, 2)
except ZeroDivisionError:
    # O bloco 'except' captura a exceção especificada (ZeroDivisionError neste caso)
    # Isso acontece se o código dentro do bloco 'try' tentar dividir por zero
    print('Não é possível dividir por zero!')
else:
    # O bloco 'else' é executado somente se nenhum erro for levantado no bloco 'try'
    # Aqui, se a divisão foi bem-sucedida e sem erros, o resultado é impresso
    print(f'Resultado: {r}')

