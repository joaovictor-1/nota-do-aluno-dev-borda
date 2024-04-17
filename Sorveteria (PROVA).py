#Exercicio 2 de 4 da atividade prática
print('Bem-vindo a sorveteria do João Victor Souza Gomes Pereira')
print('--------------------------------------CARDÁPIO----------------------------------------')
print('Número de bolas | Sabor Tradicicional (tr)| Sabor Premium (pr) | Sabor Especial (es)  ')
print('      1         |       R$6,00            |      R$7,00        |      R$8,00          ')
print('      2         |       R$10,00           |      R$12,00       |      R$14,00         ')
print('      3         |       R$14,00           |      R$17,00       |      R$20,00         ')
print('--------------------------------------------------------------------------------------')

bolas = ["1", "2", "3"]

codigos = {"tr": [6.00, 10.00, 14.00],

          "es": [7.00, 12.00, 17.00],

          "pr": [8.00, 14.00, 20.00]}

compra = []

# pedindo os dados

while True:

   quantas_bolas = input("Entre com o número de bolas desejado (1/2/3): ")

   qual_sabor = input("Entre com o sabor desejado (tr,pr,es): ")

   if quantas_bolas in bolas and qual_sabor in codigos:

       pedido = codigos[qual_sabor][bolas.index(quantas_bolas)]

       compra.append(pedido)

       algo_mais = input ("Deseja pedir mais algum sorvete? (s/digite outra tecla): ")

       if algo_mais == "s":

           continue

       else:

           break

   else:

       print("Número de bolas ou sabor inválido, tente novamente.(s)")

       continue

print ("O valor total a ser pago:", "R$",sum(compra))

