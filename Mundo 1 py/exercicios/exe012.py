# calcula o preço dos produtos para desconto

vproduto = float(input("Digite o preço do produto: R$"))

desconto = (vproduto * 15) / 100
descontado = vproduto - desconto

print(f"O preço é R${vproduto} reais e damos desconto de 15% o valor ja descontado é de R${desconto} reais")
print(f"O valor ja com o desconto aplicado é de {descontado}")
