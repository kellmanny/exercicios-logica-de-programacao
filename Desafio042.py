l1 = int(input('Qual é o tamanho do primeiro lado: '))
l2 = int(input('Qual é o tamanho do segundo lado: '))
l3 = int(input('Qual é o tamanho do terceiro lado: '))

if (l1 == l2) and (l2 == l3):
    print('EQUILÁTERO: todos os lados iguais')
elif (l1 == l2) or (l2 == l3) or (l3 == l1):
    print('ISÓSCELES: dois lados iguais, um diferente')
elif (l1 != l2) and (l2 != l3):
    print('ESCALENO: todos os lados diferentes')
