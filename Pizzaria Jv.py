print('-----------------------CARDAPIO--------------------------')
print('CODIGO | DESCRIÇÂO | PIZZA MEDIA (M) | PIZZA GRANDE (G) |')
print('     21| Napolitana|         R$ 20,00|           R$26,00|')
print('     22| Margherita|         R$ 20,00|           R$26,00|')
print('     23|  Calabresa|         R$ 25,00|           R$32,00|')
print('     24|    Toscana|         R$ 30,00|           R$39,00|')
print('     25| Portuguesa|         R$ 30,00|           R$39,00|')
print('---------------------------------------------------------')

acumulador = 0

while True:
    tamanho = input('Entre com o tamanho da pizza desejado:')
    if tamanho != 'M' and tamanho != 'G':
        print('Opção Inválida. Pare de digitar tamanhos que não existem!')
        continue #se o usuario algo invalido volta para o comeco do while
    codigo = input('Entre com o código de pizza desejado (20/21/22/23/24/25):')
    if codigo != '21' and codigo != '22' and codigo != '23' and codigo != '24' and codigo != '25':
        print('Opção inválida. Pare de digitar códigos inválidos.')
        continue

    if codigo == '21' and tamanho == 'M':
            print('Você escolheu a pizza Napolitana tamanho M')
            acumulador = acumulador + 20 # pegue o valor que tinha no acumulador e some ccom 20

    elif codigo == '21' and tamanho == 'G':
            print('Você escolheu a pizza Napolitana tamanho G')
            acumulador = acumulador + 26 #pegue o valor que tinha no acumulador e some ccom 20

    elif codigo == '22' and tamanho == 'M':
            print('Você escolheu a pizza Margherita tamanho M')
            acumulador = acumulador + 20 #pegue o valor que tinha no acumulador e some ccom 20

    elif codigo == '22' and tamanho == 'G':
            print('Você escolheu a pizza Margherita tamanho G')
            acumulador = acumulador + 26 #pegue o valor que tinha no acumulador e some ccom 20

    elif codigo == '23' and tamanho == 'M':
            print('Você escolheu a pizza Calabresa tamanho M')
            acumulador = acumulador + 25 #pegue o valor que tinha no acumulador e some ccom 20

    elif codigo == '23' and tamanho == 'G':
            print('Você escolheu a pizza Calabresa tamanho G')
            acumulador = acumulador + 39 #pegue o valor que tinha no acumulador e some ccom 20

    elif codigo == '24' and tamanho == 'M':
            print('Você escolheu a pizza Toscana tamanho M')
            acumulador = acumulador + 30 #pegue o valor que tinha no acumulador e some ccom 20

    elif codigo == '24' and tamanho == 'G':
            print('Você escolheu a pizza Toscana tamanho G')
            acumulador = acumulador + 39 #pegue o valor que tinha no acumulador e some ccom 20

    pedir_mais = input('Deseja pedir mais alguma pizza?(S/Digite outra tecla):')
    pedir_mais = pedir_mais.upper()
    if pedir_mais == 'S':
        continue
    else:
        print('o total a ser pago é: R${:.2f}' .format(acumulador))
        break





