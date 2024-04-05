""""
peça ao usuario para escrever seu nome
peça ao usuario para escrever sua idade
se o nome e idade forem digitados:
  exiba:
     seu nome é {nome}
     seu nome invertido é{nome invertido}
     seu nome contem ou nao espaços
     seu nome tem {n} letras
     a primeira letra do seu nome é {letra}
     a ultima letra do seu nome é {letra}
se nada for digitado em nome ou idade:
    exiba "desculpe, voce deixou camós vazios"    
"""


nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaço')
    else:
        print('Seu nome não contém espaço')
       
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')

else:
    print("Desculpe, voce deixou campos vazios")