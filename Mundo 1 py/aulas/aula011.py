# Colorindo o terminal

#padrão ANSI (escape sequence) \ codigo de cor

#ex: \033[style, text , bg m

#ex2: \033[0:33:44m

#style              text            BackGround

#0 None             30 Branco       40 Branco
#1 Bold             31 Vermelho     41 Vermelho
#4 Underline        32 Verde        42 Verde
#7 Negrito          33 Amarelo      43 Amarelo
#                   34 Azul         44 Azul
#                   35 Roxo         45 Roxo
#                   36 Cyano        46 Cyano
#                   37 Cinza        47 Cinza


#teste \033[0:30:41m
#teste \033[4:33:44m
#teste \033[7:35:43m
#teste \033[30:42m
#teste \033[m fundo preto com letras cinza
#teste \033[7:30m fundo branco com letra preta


# pratica

#print('\033[4;30;44m teste\033[m'.center(50))








