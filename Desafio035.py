seg1 = int(input('Primeiro valor: '))
seg2 = int(input('Segundo valor: '))
seg3 = int(input('Terceiro valor: '))

if (seg1 + seg2 > seg3) and (seg2 + seg3 > seg1) and (seg1 + seg3 > seg2):
    print('Os segmentos acima PODEM FORMAR triâgulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triâgul  o!')