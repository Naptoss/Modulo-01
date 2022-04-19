usuario = input("Digite seu usuario: ")

qtd_caracteres = len(usuario)

if qtd_caracteres < 7: 
    print('E necessario o nome do usuario ter ao menos 7 caracteres')

else:
    print("Usuario Registrado")