#aluguel de carro
print("lembrando que o valor da diaria é de R$50,00 por dia")
print("E o custo por km rodado é de 20 por km rodado\n")

dias = int(input("Quantos dias alugados? "))
km = int(input("Quantos km rodados? "))

dia = dias * 50
Km = km * 20
rs = dia + Km

print("O total a pagar é de R${:.2f}".format(rs))