numero = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão')
print('[ 1 ] Converter para BINÁRIO')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL')

num = int(input('Sua opção: '))
converter = int

if num == 1:
    converter = bin(numero)[2:]
    print(f'{numero} convertido para BINÁRIO é igual a {converter}')
elif num == 2:
    converter = oct(numero)[2:]
    print(f'{numero} convertido para OCTAL é igual a {converter}')
elif num == 3:
    converter = hex(numero)[2:]
    print(f'{numero} convertido para HEXADECIMAL é igual a {converter}')