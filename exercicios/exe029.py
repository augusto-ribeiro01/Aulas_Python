velocidade = int(input('Qual a velocidade do carro? '))

limite = 80
multa = 7

m = multa * velocidade

if velocidade > limite:
    print('Você foi mutado!')
    print(f"Sua multa foi de R${m:.2f}")
else:
    print("Você esta no limete de velocidade permitido")