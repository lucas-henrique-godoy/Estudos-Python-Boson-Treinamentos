# Módulo os (Sistema Operacional):
# O módulo os em Python é amplamente utilizado para realizar funções relacionadas a sistemas de arquivos, arquivos em geral, diretórios e outras funcionalidades do sistema operacional. 
# Com ele, podemos realizar uma série de tarefas relacionadas a arquivos, diretórios e pastas.

# Passos para usar o módulo os:
# 1. Abra o terminal.
# 2. Digite python no terminal para entrar no interpretador interativo do Python.
# 3. Importe o módulo os com o comando: import os.

# Exemplos de uso do módulo os:

# os.name -> Retorna uma string que identifica o tipo de sistema operacional. Para Windows, retorna 'nt', e para macOS ou Linux, retorna 'posix'.

# os.getcwd() -> Retorna o diretório de trabalho atual.

# os.curdir -> Um atalho que retorna '.' (o diretório atual). É preferível usar os.curdir para referência ao diretório atual, pois o Python gerencia isso internamente.

# os.listdir() -> Lista o conteúdo do diretório atual.

# os.listdir('c:\\') -> Lista o conteúdo de outro diretório, especificado no caminho (neste exemplo, a raiz do sistema).

# os.chdir('c:\\') -> Altera o diretório de trabalho para o especificado. Pode usar um caminho absoluto (desde a raiz até a pasta desejada) ou relativo (a partir do diretório atual).

# os.path.join() -> Junta dois ou mais pedaços de um caminho de arquivo, formando um caminho completo e correto para o sistema operacional.

# os.mkdir('Teste') -> Cria um diretório. No exemplo, cria a pasta 'Teste' no diretório atual.

# os.rename('c:\\Teste3', 'c:\\Teste10') -> Renomeia um diretório. No exemplo, a pasta 'Teste3' é renomeada para 'Teste10'. Se já estiver no diretório 'c:\\', pode usar apenas os.rename('Teste3', 'Teste10').

# os.rmdir(caminho) -> Remove um diretório, desde que esteja vazio.

# os.remove() -> Remove um arquivo.

# os.path.basename(path) -> Retorna o nome base do caminho fornecido, que pode ser um arquivo ou diretório.
# Exemplo:
# print(os.path.basename('C:\\Users\\SeuUsuario\\Documents\\arquivo.txt'))  # Saída: 'arquivo.txt'

# os.path.basename(os.getcwd()) -> Retorna o nome base do diretório de trabalho atual.
# Exemplo:
# print(os.path.basename(os.getcwd()))

# os.path.dirname(path) -> Retorna o caminho do diretório pai do caminho fornecido. Usado com os.getcwd(), retorna o diretório pai do diretório de trabalho atual.
# Exemplo:
# print(os.path.dirname(os.getcwd()))

# os.makedirs() -> Cria diretórios de forma recursiva (vários diretórios em uma única operação).

# os.path.exists(caminho) -> Verifica se um caminho existe ou não, retornando um valor booleano.

# os.path.isdir(caminho) -> Verifica se um item é um diretório.

# os.path.isfile(caminho) -> Verifica se um item é um arquivo.

# os.path.splitext(path) -> Obtém o nome de um arquivo e separa a extensão.
# Exemplo:
# print(os.path.splitext('arquivo.txt'))  # Saída: ('arquivo', '.txt')

# Exemplos de uso do módulo os:

# Exemplo 1: Criar pastas fora do diretório atual
# import os
# pasta_nova = 'Teste3'
# pasta_pai = 'c:\\'
# caminho_completo = os.path.join(pasta_pai, pasta_nova)
# print(caminho_completo)
# os.mkdir(caminho_completo)
# print(os.listdir())
# print(os.listdir('c:\\'))

# Exemplo 2: Criar um arquivo e listar arquivos do diretório atual
# import os
# # Criação de um novo arquivo
# manipulador = open('arq.txt', 'x')
# manipulador.close()
# print(os.listdir())
# arquivo = os.path.basename('C:\\Users\\lucasgodoy\\Desktop\\Estudos-Python-Boson-Treinamentos\\arq.txt')
# print(arquivo)
# print(os.path.splitext(arquivo))

# Biblioteca pathlib:
# A biblioteca pathlib fornece uma maneira orientada a objetos para manipulação de caminhos de arquivos e diretórios.

# Exemplo:
# import pathlib
# caminho = pathlib.Path()
# print(caminho.cwd())

# Biblioteca shutil:
# A biblioteca shutil oferece funções para manipulação de arquivos e operações relacionadas, como copiar, mover e deletar arquivos e diretórios.

# Exemplo: Remover a árvore de diretórios
# import shutil
# shutil.rmtree(caminho)

# Projeto: Renomear todos os arquivos de uma pasta usando um padrão
# import os
# os.chdir('c:\\Teste')
# print(f'Diretório atual: {os.getcwd()}')
# padrao_nome = input('Qual o padrão de nomes de arquivos a usar (sem a extensão)? ')
# for contador, arq in enumerate(os.listdir()):
#     if os.path.isfile(arq):
#         nome_arq, exten_arq = os.path.splitext(arq)
#         nome_arq = padrao_nome + ' ' + str(contador)
#         nome_novo = f'{nome_arq}{exten_arq}'
#         os.rename(arq, nome_novo)
# print('Arquivos renomeados.')
