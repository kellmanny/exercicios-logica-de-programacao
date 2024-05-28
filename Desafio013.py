salario = float(input('Qual é o seu salário? R$'))

aumento = salario * 0.15
totalsalario = salario + aumento

print(f'Um funcionário que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${totalsalario:.2f}')