# condições aninhadas

#Exemplos
'''
    if condição1:
        código/bloco1
    elif condição2: # pode ter varios mais em conjunto ao if
        código/bloco2
    else: #não contem condição
        código/bloco3
'''



nome = str(input('Qual é o seu nome? '))
if nome == 'Augusto':
    print(f'Olá {nome} como vai?')
elif nome == 'Debora':
    print(f'Olá {nome} como vai?')
else:
    print(f'Olá, prazer em te conhecer {nome}!')
