import random

print('[ 0 ] Pedra')
print('[ 1 ] Papel')
print('[ 2 ] Tesoura')

# Escolha do computador
computador = random.randint(0, 2)

# Entrada do jogador
numerojogador = int(input('Sua escolha: '))

# Exibir escolhas
opcoes = ['Pedra', 'Papel', 'Tesoura']
print(f'Computador escolheu: {opcoes[computador]}')
print(f'Você escolheu: {opcoes[numerojogador]}')

# Determinar o resultado do jogo
if numerojogador == computador:
    print('Empate!')
elif (numerojogador == 0 and computador == 2) or (numerojogador == 1 and computador == 0) or (numerojogador == 2 and computador == 1):
    print('Você venceu!')
else:
    print('Você perdeu!')
