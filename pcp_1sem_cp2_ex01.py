print("Classificação de triângulos")

A = float(input("Digite a medida de um dos lados: "))
B = float(input("Digite a medida de outro lado: "))
C = float(input("Digite a medida do último lado: "))

if B > A:
    A, B = B, A
if C > A:
    A, C = C, A

if A >= B + C:
    print("Com essas medidas, um triângulo não será formado")
else:
    if A * A == B * B + C * C:
        print("O triângulo é: retângulo")


    elif A * A > B * B + C * C:
        print("O triângulo é: obtuso")

    elif A * A < B * B + C * C:
        print("O triângulo é: agudo")
