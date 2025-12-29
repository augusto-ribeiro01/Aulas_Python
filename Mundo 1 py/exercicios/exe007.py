# Calcula a media e te fala se ta passado ou não

nota1 = int(input("Digite a primeira nota:"))
nota2 = int(input("Digite a segunda nota:"))
nota3 = int(input("Digite a terceira nota:"))

media = (nota1 + nota2 + nota3) / 2

print(f"calculando a sua media com as notas {nota1}, {nota2}, {nota3}\n")

if media >= 5:
    print("Parábens você passou", f"a media é {media}\n")
elif media < 5:
    print(f"a media é {media}", "se esforce para passar!\n")

