usuario = input("Digite seu usuario: ")

senha = int(input("Digite sua senha: "))

usuario_bd = "Antonio"

senha_bd = 123

if senha == senha_bd and usuario == usuario_bd:
    print("Login Realizado com sucesso")

else:
    print("Usuario nao encontrado. ")
    