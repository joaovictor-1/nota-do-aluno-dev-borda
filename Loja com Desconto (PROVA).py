print('Bem-vindo a loja do João Victor Souza Gomes Perira')
valor_do_produto = float(input('Entre com o valor desejado:'))
qtd = float(input('Entre com a quantidade desejada:'))
desconto = 0
# Teste em cima da variável quantidade
if qtd < 5: #Outra maneira de if qtd < 5:
    desconto_produto = 0
elif 5 <= qtd < 21:   #if(qtd>= 5) and (qtd<20)
    desconto= 0.03    #3% = 0.03 || 100% = 1.00
elif 21 <= qtd < 101: #if(qtd >=20) and (qtd <100)
    desconto = 0.06   #6% = 0.06 || 100% = 1.00
else:
    desconto= 0.10    #10% = 0.10


total_sem_desconto = valor_do_produto * qtd
print('O valor total SEM desconto é de: R$ {:.2f}' .format(total_sem_desconto))
total_com_desconto = total_sem_desconto - total_sem_desconto * desconto
print('O valor total COM desconto é de: R$ {:.2f}' .format(total_com_desconto))

