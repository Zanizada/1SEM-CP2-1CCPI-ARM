print("Digite abaixo as informações do cliente.")
nome = input("Nome: ")
idade = int(input("Idade: "))
renda = float(input("Renda mensal: "))
valor_emprestimo = float(input("Valor desejado do empréstimo: "))
parcelas = int(input("Número de parcelas (de 3 à 24): "))

juros = [0.05, 0.08, 0.10]

if idade > 18 and valor_emprestimo <= 20 * renda:
    if parcelas <= 6:
        juro = juros[0]
    elif 6 < parcelas <= 12:
        juro = juros[1]
    else:
        juro = juros[2]

    valor_parcela = valor_emprestimo * (juro*(1+juro)**parcelas)/((1+juro)**parcelas-1)
else:
    print("Empréstimo negado.")