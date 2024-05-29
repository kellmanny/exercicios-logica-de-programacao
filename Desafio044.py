preco = float(input('Preço das compras: R$'))
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x no cartão')
opcao = int(input("Qual a sua opção? "))

desconto = float
juros = float
total = float

if opcao == 1:
    desconto = (preco * 10) / 100
    valor = preco - desconto
    print(f'O valor a ser pago é R${valor:.2f}')
elif opcao == 2:
    desconto = (preco * 5) / 100
    valor = preco - desconto
    print(f'O valor a ser pago é R${valor:.2f}')
elif opcao == 3:
    print(f'O valor a ser pago é R${preco:.2f}')
elif opcao == 4:
    juros = (preco * 20) / 100
    valor = preco + juros
    print(f'O valor a ser pago é R${valor:.2f}')