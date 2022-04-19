horario = input("Digite um horario valido (0-23): ")
if horario.isdigit():
    horario = int(horario)
    if horario < 0 and horario > horario:
        print("Insira um horario entre 0 e 23")
    if horario <= 11:
        print("Bom dia")
    elif horario <= 17:
        print("Boa Tarde")
    else:
        print("Boa noite")

else:
    print("ERRO, insira um horario valido")
