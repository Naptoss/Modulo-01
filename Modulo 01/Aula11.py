nome = input("Digite seu nome: ")

qtd_caracteres = len(nome)

if qtd_caracteres <= 4:
    print("Seu nome e curto")

elif qtd_caracteres <= 6:
    print("Seu nome e normal")

else:
    print("Seu nome e grande")