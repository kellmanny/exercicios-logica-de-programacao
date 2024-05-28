salario = float(input('Digite o valor do seu sálario? R$'))

maior = 0.10 * salario
menor = 0.15 * salario
aumento = float

if salario <= 1250:
    aumento = menor + salario
    print(f'Quem ganhava R${salario} passa a ganhar R${aumento:.2f} agora.')
else:
    aumento = maior + salario
    print(f'Quem ganhava R${salario} passa a ganhar R${aumento:.2f} agora.')