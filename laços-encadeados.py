# EXEMPLO 1: Laços Aninhados

# Laço externo que itera de 1 a 5 (inclusive)
for cont_externo in range(1, 6):
    # Imprime o número da rodada
    print(f'\nRodada: {cont_externo}')
    
    # Laço interno que itera de 5 a 1 (inclusive), com passo -1
    for cont_interno in range(5, 0, -1):
        # Imprime o valor atual do laço interno
        print(f'Valor: {cont_interno}')

# Mensagem exibida após os laços
print('Fim dos Laços!')

# ____________________________________________________________________________________________________________________________

# EXEMPLO 2: Uso de Números Aleatórios com Módulo random

# Importa o módulo random para gerar números aleatórios
import random

# Laço externo que itera de 1 a 5 (inclusive)
for A in range(1, 6):
    # Imprime o conjunto atual
    print(f'\nConjunto {A}')
    
    # Laço interno que itera 5 vezes
    for B in range(5):
        # Gera um número aleatório entre 1 e 100
        num = random.randint(1, 100)
        # Imprime o valor do número gerado
        print(f'Valor do número: {num}')
