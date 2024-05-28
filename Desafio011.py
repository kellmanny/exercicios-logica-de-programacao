largura = float(input('largura da parede? '))
altura = float(input('altura da parede? '))

metroQ = float(largura * altura)

resultado = float(metroQ / 2)
print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {metroQ}m² .')
print(f'Para pintar essa parede, você precisará de {resultado}l de tinta.')