def soma(x, y):
    return x + y

# Este bloco será executado somente quando o módulo modulo_soma.py for executado diretamente, por exemplo, se você rodar este arquivo como um script.
# Se modulo_soma.py for importado por outro arquivo, o código dentro deste bloco não será executado. 
# Isso previne que os prints abaixo apareçam no terminal quando o módulo for importado, evitando possíveis efeitos indesejados.

if __name__ == '__main__': 
    # Exemplos de testes para verificar se a função soma está funcionando corretamente.
    # Estes prints mostram o resultado da função soma com diferentes entradas para validação.
    print(soma(10, 20)) # Imprime o resultado da soma de 10 e 20, que é 30.
    print(soma(10, 30)) # Imprime o resultado da soma de 10 e 30, que é 40.
    print(soma(10, 40)) # Imprime o resultado da soma de 10 e 40, que é 50.
