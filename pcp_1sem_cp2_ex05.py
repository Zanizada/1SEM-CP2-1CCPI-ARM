def pode_aprovar(idade, renda, valor):
    if idade >= 18 and valor <= (20 * renda):
        return True
    else:
        return False

def definir_taxa(parcelas):
    juros = [0.05, 0.08, 0.10]
    if parcelas <= 6:
        juro = juros[0]
    elif 6 < parcelas <= 12:
        juro = juros[1]
    else:
        juro = juros[2]
    return juro

def calcular_parcela(valor, taxa, parcelas):
    return valor * (taxa*(1+taxa)**parcelas)/((1+taxa)**parcelas-1)

def calcular_total(parcela, parcelas):
    return parcela * parcelas

def calcular_juros(total, valor):
    return total - valor

print("Digite abaixo as informações do cliente.")
nome = input("Nome: ")
idade = int(input("Idade: "))
renda_mensal = float(input("Renda mensal: "))
valor_emprestimo = float(input("Valor desejado do empréstimo: "))
n_parcelas = int(input("Número de parcelas (de 3 à 24): "))

if pode_aprovar(idade, renda_mensal, valor_emprestimo):
    juros = definir_taxa(n_parcelas)
    valor_parcela = calcular_parcela(valor_emprestimo, juros, n_parcelas)
    total = calcular_total(valor_parcela, n_parcelas)
    juros_totais = calcular_juros(total, valor_emprestimo)
    print("Empréstimo aprovado.")
    print(f"Cliente: {nome}.\nValor financiado: R$ {valor_emprestimo:.2f}.\nTaxa de juros aplicada: {int(juros*100)}%.\nValor da parcela: R$ {valor_parcela:.2f}.\nValor total pago: R$ {total:.2f}.\nTotal de juros pagos: R$ {juros_totais:.2f}.")
else:
    print("Empréstimo negado.")