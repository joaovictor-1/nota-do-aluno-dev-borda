km = int(input('Quantos Km foram percorridos?'))
dias = int(input('Quantos dias foram percorridos?'))

preco= 60 * dias + 0.15 * km
print('Km= {} Dias: {}' .format(km,dias))
print('Valor a ser pago: {}' .format(preco))