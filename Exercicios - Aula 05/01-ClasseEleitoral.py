ida = int(input('Digite sua idade: '))

if ida < 16:
    input('Não-eleitor.')
elif ida >= 18 and ida <= 65:
    input('Eleitor obrigatório. ')
else:
    print('Eleitor facultativo. ')
