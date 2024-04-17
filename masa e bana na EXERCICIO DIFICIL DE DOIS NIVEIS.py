print('Escolha o que deseja comprar:')
print('1 - Maçã')
print('2 - Laranja')
print('3 - Banana')
produto = int(input('Qual sua escolha?'))
qtd = int(input('Quantas você irá comprar?'))
if (produto == 1):
  pagar = qtd * 2.3
  print('Voce comprou {} maçãs. Total á pagar: {}' .format(qtd, pagar))
elif (produto == 2):
      pagar = qtd * 3.6
      print('Voce comprou {} laranjas. Total á pagar: {}' .format(qtd, pagar))
elif (produto == 3):
    pagar= qtd * 1.85
    print('Voce comrpou {} bananas. Total á pagar {}' .format(qtd, pagar))
else:
    print('Produto inxexistente')
