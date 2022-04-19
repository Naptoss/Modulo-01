
nome = input("Insira seu nome: ")

print()

print('Nome registrado')

print()

idade = input("Insira sua idade para o emprestimo: ")
print(f'idade registrada Sr.{nome} ')

idade = int(idade)



print()

idade_menor = 20
idade_maior = 30

if idade_menor >=  idade <= idade_maior:
    print("Desculpa, idade minima não atingida.") 
    
else:
   print("Idade minima autorizada ")