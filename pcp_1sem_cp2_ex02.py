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
    print("NAO FORMA TRIANGULO")
else:
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")


    elif A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")

    elif A**2 < B**2 + C**2:
        print("TRIANGULO ACUTANGULO")

    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif B == C or B == A:
        print("TRIANGULO ISOSCELES")
