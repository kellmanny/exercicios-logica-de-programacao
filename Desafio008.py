distancia = float(input('Uma distancia em metros: '))
print(f'A medida de {distancia}m corresponde a')

km = distancia / 1000
hm = distancia / 100
dam = distancia / 10
dm = int (distancia * 10)
cm = int (distancia * 100)
mm = int (distancia * 1000)

print(f'{km}km')
print(f'{hm}hm')
print(f'{dam}dam')
print(f'{dm}dm')
print(f'{cm}cm')
print(f'{mm}mm')