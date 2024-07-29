# Exceção é um objeto que representa um erro que ocorreu ao executar o programa.
# Blocos try ... except


# EXXEMPLO 1 - CAPTURANDO 1 EXCEÇÃO
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
else: # Opcional, não necessariamente precisamos utiliza-lo
    # O bloco 'else' é executado somente se nenhum erro for levantado no bloco 'try'
    # Aqui, se a divisão foi bem-sucedida e sem erros, o resultado é impresso
    print(f'Resultado: {r}')

#____________________________________________________________________________________________________________________________
# EXEMPLO 2 - CAPTURANDO VÁRIAS EXCEÇÕES

def div(k, j):
    # Função que divide k por j e retorna o resultado arredondado para 2 casas decimais.
    return round(k / j, 2)

if __name__ == '__main__':
    # Bloco de código principal que será executado se o script for executado diretamente.

    while True: # Loop Infinito
        # Loop infinito que continuará a solicitar entradas do usuário até que ambos os números sejam digitados corretamente.
        # O loop só sairá quando o usuário fornecer dois números inteiros válidos.
        try:
            # Solicita ao usuário para digitar dois números e tenta convertê-los para inteiros.
            n1 = int(input('Digite um número: '))
            n2 = int(input('Digite outro número: '))
            break  # Sai do loop se ambos os números foram lidos e convertidos corretamente.
        except ValueError:
            # Captura exceções do tipo ValueError (ocorre quando a conversão para int falha).
            print(f'Ocorreu um erro ao ler o valor. Tente novamente.')  # Informa ao usuário que a entrada foi inválida.

    try:
        # Tenta realizar a divisão utilizando a função div e passando n1 e n2 como argumentos.
        r = div(n1, n2)  # Corrigido para passar n1 e n2 diretamente.
    except ZeroDivisionError:
        # Captura exceções do tipo ZeroDivisionError (ocorre quando n2 é zero).
        print('Não é possível dividir por zero!')  # Informa ao usuário que a divisão por zero não é permitida.
    except:
        # Captura qualquer outra exceção não prevista/ EXCEÇÃO GENÉRICA.
        print('Ocorreu um erro desconhecido...')  # Informa ao usuário sobre um erro desconhecido.
    else:
        # Executado se não ocorrer nenhuma exceção no bloco try.
        print(f'Resultado: {r}')  # Exibe o resultado da divisão.
    finally:
        print(f'\nFim do cálculo') # Executa sempre, independente se houver ou não uma exceção.
