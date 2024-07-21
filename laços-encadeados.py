# LAÇOC ENCADEADOS
# - EXEMPLO 1:

# for cont_externo in range(1,6):
#     print(f'\nRodada: {cont_externo}')
#     for cont_interno in range(5, 0, -1):
#         print(f'Valor: {cont_interno}')

# print('Fim dos Laços!')

#____________________________________________________________________________________________________________________________

# - EXEMPLO 2:

import random

for A in range(1,6):
    print(f'\nConjunto {A}')
    for B in range(5):
        num = random.randint(1,100)
        print(f'Valor do número: {num}')