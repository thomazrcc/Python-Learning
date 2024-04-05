"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número: ')

if numero.isdigit():
    numero_int = int(numero)
    par_impar = numero_int % 2 == 0
    par_impar_text = 'ímpar'

    if par_impar:
        par_impar_text = 'Par'

    print(f'O número {numero_int} é {par_impar_text}')
else:
    print('Você não digitou um numero inteiro')
    

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""


numero = input('Digite a hora em números inteiros: ')
try:
    hora = int(numero)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    
    elif hora >= 12 and hora <= 17:
        print('Boa tarde')

    elif hora >= 18 and hora <= 23:
        print('Boa noite')

    else:
        print('Não conheço essa hora')
     
except:
    print('Por favor digite apenas números inteiros')
     

""""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome: ')
tam_nome = len(nome)

curto = tam_nome > 1 and tam_nome <= 4
normal = tam_nome > 4 and tam_nome <=6


if curto :
    print('Seu nome é curto')
elif normal:
    print('Seu nome é normal')
else: print('Seu nome é muito grande')



    