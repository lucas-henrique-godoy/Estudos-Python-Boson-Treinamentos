# Módulo os: Muito empregado a realização de funções relacionadas a sistemas de arquivos, arquivos em geral, diretórios, e outras funcionalidades de sistema operacional. Podemos fazer uma série de tarefas relacionadas a arquivos, diretórios e pastas, etc. Para usar o módulos devemos seguir os seguintes passos:
# 1 - Abrir o terminal,
# 2- Digitar py no terminal para entrar no interpretador interativo do python,
# 3- Importar o módulo os digitando: import os.
# EXEMPLOS:

# os.name -> Retorna uma string relacionada ao tipo do sistema operacional se for Windows retorna'nt', e se for MAC ou Linux retorna 'posix'.

# os.getcwd() -> Retorna qual o diretório atual em que o código esta aberto.

# os.curdir -> É um atalho. Retorna um ponto '.' , que siginifica um atalho para o diretório atual, quando eu quiser realizar algum tipo de tarefa que faça referencia direta ao diretorio atual(aberto), eu posso utilizar o ponto ou escrever os.curdir(mais indicado pois o próprio pytohn gerencia isso.)

# os.listdir() -> Visualizar o conteúdo do diretorio atual. 

# os.listdir('c:\\') -> Visualizar o conteúdo de outro diretorio que não seja o diretório atual. (Neste caso visualizando o que tem na raiz do meu sistema). 

# os.chdir('c:\\') -> Mudar de diretório, pode ser um absoluto ou relativo. (Neste exemplo mudou para o diretório raiz do drive C: em sistemas Windows, se quiser ver o diretorio atual é so usar os.getcwd e vera que que esta na raiz).

# os.mkdir('Teste') -> Cria uma pasta.(Neste exemplo nós criamos uma pasta chamada Teste no diretorio razi do drive C:)

# os.-> Criar pastas fora sem  do diretório atual, mas sem sair do mesmo.
