altura = float(input('Digite sua altura: (m) '))
peso = float(input('Digite seu peso: (Kg) '))

imc = peso / (altura * altura)

print(f'Sua altura é de {altura:.2f}m')
print(f'Seu peso é de {peso:.1f} Kg')
print(f'Seu Índice de massa corporal é de {imc:.1f} ')

if (imc >= 18.5) and (imc < 25):
    print('Peso ideal')
elif imc < 18.5:
    print('Abaixo do Peso')
elif (imc >= 25) and (imc < 30):
    print('Sobrepeso')
elif (imc >= 30) and (imc < 40):
    print('Obesidade')
elif imc >= 40:
    print('Obesidade Mórbida')

