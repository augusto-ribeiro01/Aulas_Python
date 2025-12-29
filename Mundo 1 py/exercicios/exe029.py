velocidade = float(input('Qual a velocidade do carro? '))

limite = 80
multa = 7

m =  (velocidade-80) * multa

if velocidade > limite:
    print('Você excedeu o limete de velocidade 80km/h')
    print('Você foi mutado!')
    print(f"Sua multa foi de R${m:.2f}")
else:
    print("Você esta no limete de velocidade permitido")