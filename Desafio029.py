velocidade = int(input('Qual a velocidade do carro? '))
multa = 80
valor = velocidade - multa

if velocidade >= 80:
    total = valor * 7
    print(f'Você deve pagar uma multa de R${total:.2f}!')
else:
    print('Tenha um bom dia! Dirija com segurança!')
