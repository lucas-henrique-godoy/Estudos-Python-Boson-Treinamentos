# Quando este arquivo (app.py) é executado, somente o código neste arquivo será executado. 
# O código dentro do bloco if __name__ == '__main__': no módulo importado (modulo_soma.py) não será executado.
# Se o bloco if __name__ == '__main__': não estivesse presente em modulo_soma.py, qualquer código fora de funções ou classes seria executado também, 
# o que poderia causar efeitos indesejados ao importar o módulo.

from modulo_soma import soma 

a = 10
b = 50
print(soma(a,b))
