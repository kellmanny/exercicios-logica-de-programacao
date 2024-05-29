num1 = int(input('Escolha um número inteiro: '))
num2 = int(input('Escolha outro número inteiro: '))

if num1 > num2:
    print('O primeiro valor é maior')
elif num2 > num1:
    print('O Segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')