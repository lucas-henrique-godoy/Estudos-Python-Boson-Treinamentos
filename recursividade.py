# Recursividade

# Fórmula geral para o fatorial:
# fatorial(num) = 1, se num = 0 ou se num = 1 'Caso-Base' -  Precisa ser identificado e é o que finaliza o cálculo recursivo, na qual o problema é tão simples que a resposta ja é direta. No caso do fatorial se o número fornecido for 0 ou 1 a resposta ja é direta, por convenção o fatorial é 1.
# fatorial(num) = num * fatorial(num - 1 seu antecessor), para num > 1 'Caso Recursivo- caso que chama a si próprio, só que pra uma versão menor do problema diversa vezes sucessivamente até chegar no Caso-Base '
# EX:
# 4! → 4 * fatorial(3) = 4 * 3 * fatorial(2) = 4 * 3 * 2 * fatorial(1) →
# 4! = 4 * 3 * 2 * 1 = 24


# Define a função para calcular o fatorial de um número
def fatorial(numero):
    # Verifica se o número é 0 ou 1, pois o fatorial de 0 e 1 é 1
    if numero == 0 or numero == 1:
        return 1
    else:
        # Caso contrário, calcula o fatorial usando a recursividade
        return numero * fatorial(numero - 1)

# Esta parte do código só será executada se o script for executado diretamente
if __name__ == '__main__':
    # Solicita ao usuário um número inteiro positivo para calcular o fatorial
    x = int(input('Digite um número inteiro positivo para calcular seu fatorial: '))
    
    try:
        # Tenta calcular o fatorial do número fornecido
        res = fatorial(x)
    except RecursionError:
        # Se ocorrer um erro de recursão (geralmente devido a um número muito grande ou negativo)
        print(f'O número fornecido é muito grande ou negativo.')
    else:
        # Se o cálculo for bem-sucedido, exibe o resultado
        print(f'O fatorial de {x} é: {res}')
    finally:
        # Esta parte sempre será executada, independentemente de sucesso ou erro
        print(f'Cálculo finalizado!')
