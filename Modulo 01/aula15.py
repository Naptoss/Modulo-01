from signal import valid_signals
from unicodedata import digit


secreto = "helicoptero"
digitadas = []
vidas = 3

while True:
    if vidas < 0:
        print("Voce perdeu")
        break

    letra = input("Digite uma letra: ")

    if len(letra) > 1:
        print("Nao vale, digite apenas uma letra. ")
        continue


    digitadas.append(letra)

    if letra in secreto :
        print(f'Que legal, a letra "{letra}", existe na palavra secreta. ')
    else:
        print(f'Poxa, a letra "{letra}" não existe na palavra secreta.')
        digitadas.pop()
    print(digitadas)
    
    secreto_temporario = '' 
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    if secreto_temporario == secreto:
        print(f"Que legal, voce ganhou !!!! a palavra era {secreto_temporario} ")
        break
    else:
        print(f'A palavra secreta assim {secreto_temporario}')
    
    if letra not in secreto:
        vidas -= 1
    print(f'Voce ainda tem {vidas} vidas restantes. ')  
    print()
    