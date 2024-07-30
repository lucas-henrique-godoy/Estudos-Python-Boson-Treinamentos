#   FORÇANDO UMA EXCEÇÃO NO MOMENTO ADEQUADO.

#from math import sqrt  # Importa a função sqrt da biblioteca math para calcular a raiz quadrada de um número.

#if __name__ == '__main__':
    # Este bloco de código será executado somente se o script for executado diretamente, não se for importado como um módulo.

    #while True:
        # Inicia um loop infinito que continuará a solicitar entradas do usuário até que um número positivo seja fornecido.  
#        try:
            # Solicita ao usuário para digitar um número e tenta convertê-lo para inteiro.
#            num = int(input('Digite um número positivo: '))
            
            # Verifica se o número é negativo e lança uma exceção se for.
#            if num < 0:
#                raise ArithmeticError
#        except ArithmeticError:
            # Captura a exceção se um número negativo for fornecido.
#            print(f'Foi fornecido um número negativo!')  # Informa ao usuário sobre o erro.
#        else:
            # Executa se não houver exceções. Calcula e imprime a raiz quadrada do número.
#            print(f'A raiz quadrada de {num} é {sqrt(num)}')  
#            break  # Sai do loop após o cálculo bem-sucedido.
#        finally:
            # Executa sempre, independentemente de ter ocorrido uma exceção ou não.
#            print(f'Fim do cálculo.')  # Informa que o cálculo terminou.

#_______________________________________________________________________________________________________________________

# EXCEÇÕES CRIADAS PELO USUÁRIO:
from math import sqrt  # Importa a função sqrt da biblioteca math para calcular a raiz quadrada de um número.

# Define uma nova exceção personalizada chamada NumeroNegativoError, que eu criei.
class NumeroNegativoError(Exception):
    def __init__(self):
        # Inicializador da exceção personalizada. Neste caso, não faz nada além de inicializar a exceção.
        pass 

if __name__ == '__main__':
    # Verifica se o script está sendo executado diretamente. O código dentro deste bloco será executado apenas se o script for executado diretamente.
    
    try:
        # Tenta executar o código abaixo, que pode levantar uma exceção se algo der errado.
        num = int(input('Digite um número positivo: '))
        # Solicita ao usuário para digitar um número e tenta convertê-lo para um inteiro.
        
        if num < 0:
            # Verifica se o número é negativo.
            # Se for, lança a exceção personalizada NumeroNegativoError.
            raise NumeroNegativoError
    except NumeroNegativoError:
        # Captura a exceção NumeroNegativoError se um número negativo for fornecido.
        # Este bloco é executado quando a exceção personalizada é levantada.
        print(f'Foi fornecido um número negativo!')  # Informa ao usuário que o número fornecido é negativo e solicita uma nova entrada.
    else:
        # Este bloco é executado se nenhum erro ocorrer no bloco try.
        # Calcula e imprime a raiz quadrada do número positivo fornecido.
        print(f'A raiz quadrada de {num} é {sqrt(num)}')  
    finally:
        # Este bloco é executado independentemente de ter ocorrido uma exceção ou não.
        # Imprime uma mensagem final para indicar que o cálculo foi finalizado.
        print(f'Fim do cálculo.')  



# OBS: pass- # Instrução que diz: 'Não tem nada aqui, passe a diante, ignore'. É da mesma familia do 'continue' e do 'break'.
# É usado geralmente quando você esta criando um tipo de bloco de código, mas naquele momento exato você ainda não vai preencher
# o código do bloco, mas precisa testar a aplicação sem erros