valor_int = input("Digite um valor inteirio: ")

if valor_int.isdigit():
    valor_int = int(valor_int)
    if valor_int % 2 == 0:
        print("Esse numero e par")
    else:
        print("essse numero e impar")
else:
    print("ERRO, por gentileza utileze de um numero inteiro")

