from datetime import date
nascimento = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento
falta = 18 - idade
sera = atual + falta
deveria = atual - nascimento - 18
foi = atual - deveria

if idade == 18:
    print(f'Quem nasceu em {nascimento} tem {idade} em {atual}.')
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    print(f'Quem nasceu em {nascimento} tem {idade} em {atual}.')
    print(f'Ainda faltam {falta} anos para o alistamento')
    print(f'Seu alistamento será em {sera}')
elif idade > 18:
    print(f'Quem nasceu em {nascimento} tem {idade} em {atual}.')
    print(f'Você deveria ter se alistado há {deveria} anos')
    print(f'Seu alistamento foi em {foi}')

