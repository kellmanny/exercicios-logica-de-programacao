import math

catetoOposto = float(input('Digite o comprimento do cateto oposto: '))
catetoAdjacente = float(input('Digite o comprimento do cateto oposto: '))

c1 = catetoOposto * catetoOposto
c2 = catetoAdjacente * catetoAdjacente

r = math.sqrt(c1 + c2)

print(f'A hipotenusa vai medir {r:.2f}')