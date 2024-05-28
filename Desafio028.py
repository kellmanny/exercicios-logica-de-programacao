from random import randint

print('-------ADIVINHE QUAL NÚMERO ESTOU PENSANDO ENTRE 0 À 5------------')
computador = randint(0,5)
numero = int(input("Digite o número: "))
print(f'Pensei no número {computador}')
if computador == numero:
    print('Você acertou')
else:
    print('Você errou')


