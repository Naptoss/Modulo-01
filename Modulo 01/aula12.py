trava =  "sabia que a mãe do sabiá não sabia que o sabiá sabia assobiar?"
qtd_caracteres = len(trava)
contador = 0
nova_str = ''

usuario = input("Qual letra gostaria de deixar maiuscula?: ")

while contador < qtd_caracteres:
    letra = trava[contador]
    if letra == usuario:
        nova_str += usuario.upper()
    else:
        nova_str += letra
    contador += 1


print(nova_str)    
