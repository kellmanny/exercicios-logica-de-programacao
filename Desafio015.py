dias = float (input('Quantos dias alugados? '))
kgPercorridos = float (input('Digite  a quantidade Km percorridos: '))

valorPorDia = dias * 60
kmRodado = kgPercorridos * 0.15

total = valorPorDia + kmRodado
print(f'O total a pagar é de R${total:.2f}')