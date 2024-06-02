soma = 0  # Inicializa a variável soma com zero para armazenar a soma dos números que atendem à condição.
cont = 0  # Inicializa a variável cont com zero para contar quantos números atendem à condição.

# Loop for que itera sobre os números ímpares de 1 a 500, de dois em dois.
for c in range(1, 501, 2):
    # Verifica se o número atual é divisível por 3.
    if c % 3 == 0:
        cont += + 1  # Incrementa o contador se o número atual atender à condição.
        soma += + c  # Adiciona o número atual à soma se ele atender à condição.

# Imprime a soma total e o número de valores que atenderam à condição.
print(f'A soma de todos os {cont} valores solicitados é {soma}')

