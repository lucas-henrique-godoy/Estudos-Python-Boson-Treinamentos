# Exemplo de uso dos operadores lógicos em Python

# AND
# Verifica se a idade é maior ou igual a 18 e a altura é maior ou igual a 1.70
idade = 15
altura = 1.75
resultado = (idade >= 18) and (altura >= 1.70) 
msg = 'Pode participar do evento? ' + str(resultado)
print(msg)  # Saída: Pode participar do evento? False (porque a idade não é maior ou igual a 18)

# OR
# Programa de disparo de alarme
# Verifica se a porta está aberta OU a janela está aberta
porta = 'fechado'
janela = 'aberto'
alarme = (porta == 'aberto') or (janela == 'aberto')
msg = 'Alarme Disparado? ' + str(alarme)
print(msg)  # Saída: Alarme Disparado? True (porque a janela está aberta)

# NOT
# Verifica se tem dinheiro (inicialmente False) e depois inverte o valor com NOT
tem_dinheiro = False
tem_dinheiro = not tem_dinheiro
msg = 'Tem dinheiro? ' + str(tem_dinheiro)
print(msg)  # Saída: Tem dinheiro? True (porque o valor de tem_dinheiro foi invertido para True)
