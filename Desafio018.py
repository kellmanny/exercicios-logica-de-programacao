import  math
ângulo  = float(input('Digite um ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))
print(f'O ângulo de {ângulo} tem o Seno de {seno:.2f}')
cosseno = math.cos(math.radians(ângulo))
print(f'O ângulo de {ângulo} tem o COSSENO de {cosseno:.2f}')
tangente = math.tan(math.radians(ângulo))
print(f'O ângulo de {ângulo} tem o TANGENTE de {tangente:.2f}')