distancia = float(input('Qual a distância da sua viagem? '))

maior = 0.45
menor = 0.50

total = float

print(f'Você está preste a fazer uma vigem de {distancia:.1f}Km')

if distancia <= 200:
    total = menor * distancia
    print(f'E o preço da sua passagem será de R${total:.2f}')
else:
    total = maior * distancia
    print(total)
