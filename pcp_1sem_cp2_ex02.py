print("Classificação de triângulos")

A = float(input("Digite a medida de um dos lados: "))
B = float(input("Digite a medida de outro lado: "))
C = float(input("Digite a medida do último lado: "))

if B > A:
    A, B = B, A
if C > A:
    A, C = C, A
if C > B:
    B, C = C, B

if A >= B + C:
    print("Com essas medidas, um triângulo não será formado")
else:
    if A**2 == B**2 + C**2:
        print("O triângulo é: retângulo")


    elif A**2 > B**2 + C**2:
        print("O triângulo é: obtuso")

    elif A**2 < B**2 + C**2:
        print("O triângulo é: agudo")

    if A == B == C:
        print("e tambem é equilátero")
    elif B == C or B == A:
        print("e tambem é isósceles")
