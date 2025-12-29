# converso

number = float(input("quanto de dinheiro você tem na carteira? R$"))

dolar = number / 5.42
euro = number / 6.37
yuan = number / 0.77


print("Com R${:.2f} você pode comprar U${:.2f}\n".format(number, dolar))
print("Com R${:.2f} você pode comprar £${:.2f}\n".format(number, euro))
print("Com R${:.2f} você pode comprar Y${:.2f}".format(number, yuan))