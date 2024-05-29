n1 = float(input('Quanto foi a primeira nota? '))
n2 = float(input('Quanto foi a segunda nota? '))

media = (n1 + n2) / 2

if (media < 6.9) and (media > 5):
    print('RECUPERAÇÃO')
elif media >= 7:
    print('APROVADO')
else:
    print('REPROVADO')

print(f'A sua nota foi: {media}')