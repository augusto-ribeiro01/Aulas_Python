# cadeia de caracteres  # Manipulação de texto

# fatiamento

'''ex:

frase = 'curso em video python'

frase[9:14]

frase[9:21:2] pula de 2 em 2

frase[:5] ele começa do caracter 0 até 5

frase[15:] ate o final se não souber o ultimo caracter

frase[9::3] começa no 9 e vai até o final pulando de 3 em 3
'''



# análese

'''
len(frase) retorna o tamanho da frase

frase.count('o') conta quantas letra especificada ela existe
frase.count('o', 0, 13) entre o 0 e o 13 quantas letra expecificada existe na frase

frase.find('deo') diz quantas vezes ele encontra oq especificou, na frase

frase.find('android') retonara -1 pq não esta na frase

'curso'in frase ele vai retorna true

'''


# transformação

'''
frase.replace('python', 'android') subistitui o primeiro pelo segundo

frase.upper() troca tudo para MAIUSCULAS

frase.capitalize() retorna uma frase em minuscula e so a primeira letra que começa a frase em maiuscula

frase.title() quantas palafras tem e vai colocar a inicial de cada palafra em maiusculo

frase'   Aprenda Python  '

frase.strip() remove os espaços desnecessarios/inuteis como na frase 

frase.rstrip() começa pela direita

frase.lstrip começa pela esquerda

'''

# junção

'''
'-'join(frase) retira os espaços da frase

'''

'''frase = 'curso em video python'
print(frase.replace('curso em video python', 'programar em python é foda'))'''

'''frase = 'curso em python'
dividido = frase.split()
print(dividido)'''