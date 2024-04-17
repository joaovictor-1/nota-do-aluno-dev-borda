#Exercicio 1
def borda(s1):
    tam = len(s1)
    if tam:
        print('+','-' * tam, '+')
        print('|', s1, '|')
        print('+', '-' * tam, '+')


#Programa principal
borda('Olá, mundo!')
borda ('lógica de Programação e Algoritmos')
