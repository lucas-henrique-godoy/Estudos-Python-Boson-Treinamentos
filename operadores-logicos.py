# idade = 15
# altura = 1.75

# resultado = (idade >= 18) and (altura >= 1.70) 
# msg = 'Pode participar do evento? ' + str(resultado)

# print(msg)

# Programa de disparo de alarme
porta = 'fechado'
janela = 'fechado'

alarme = (porta == 'aberto') or (janela == 'aberto')
msg = 'Alarme Disparado? ' + str(alarme)
print(msg)