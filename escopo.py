# Definição de uma variável global
var_global = "Curso Completo de Python"

# Função que modifica e utiliza variáveis globais e locais
def escreve_texto():
    # Declara que queremos usar a variável global 'var_global' dentro desta função.
    # Sem essa declaração, se tentássemos modificar 'var_global' aqui, 
    # Python criaria uma nova variável local chamada 'var_global' dentro da função, 
    # e a variável global original não seria alterada.
    global var_global
    
    # Modifica a variável global 'var_global' dentro da função.
    # Agora, o valor da variável global 'var_global' será alterado para "Bancos de Dados com SQL".
    var_global = "Bancos de Dados com SQL"
    
    # Define uma variável local dentro da função
    var_local = "Fábio dos Reis"
    
    # Imprime o valor da variável global que foi modificada
    print(f'Variável Global: {var_global}')
    
    # Imprime o valor da variável local que só existe dentro desta função
    print(f'Variável Local: {var_local}')


# Bloco de código que será executado se este arquivo for o principal
if __name__ == '__main__':
    # Imprime uma mensagem indicando que a função será chamada
    print(f'Executar a função escreve_texto()')
    
    # Chama a função que modifica a variável global e define uma variável local
    escreve_texto()

    # Imprime uma mensagem indicando que tentará acessar variáveis diretamente
    print('Tentar acessar as variáveis diretamente')
    
    # Imprime a variável global. A mudança feita na função será refletida aqui
    print(f'Variável Global: {var_global}')
    
    # Tentar acessar a variável local fora da função resultaria em um erro, então esta linha está comentada
    # print(f'Variável Local: {var_local}')  # Esta linha causará um erro
