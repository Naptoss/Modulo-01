"""
Tipos de dados 
str - string - textos 'Assim' "Assim"
int - inteiro - 123456 0 -10 -20 -50 -60 -15000 1500
float - real/ponto flutuante - 10.50 1.5 -10.10 -50.93 0.0
bool - booleano/lógico - True/false 10 == 10
"""
idade = int

nome = input('Digite seu nome: ',)
print(f'Seja Bem-vindo(a) {nome.title()}') 

idade = input('Digite a sua idade: ')
print('idade registrada')

altura =float(input('Digite sua altura: '))
print('altura registrada')

peso = float(input('Quantos kg você tem ?: '))
print('peso registrado')

imc = peso / (altura **2)

print(f'O {nome.title()} tem {idade} anos de idade e seu IMC é de {imc:.2f} ')



imc_abaixo =  16.0 >= 17.9
imc_saudavel = 18.7 <= 24.1 
imc_sobrepeso = 24.45 <= 39.0   

if imc_abaixo <= imc:
    print("Você esta abaixo do peso ideal") 

elif imc <= imc_saudavel: 
    print ("Você esta no peso ideal")  

else:   
 print("Você esta sobrepeso")


