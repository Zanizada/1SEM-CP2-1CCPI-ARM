print("Cálculo do salário final")

nome = input("Digite seu nome: ")
cargo = input("Digite seu cargo: ").lower().strip()
salario = float(input("Digite seu salario base: "))
horas_extras = int(input("Digite a quantidade de horas extras trabalhadas: "))
faltas = int(input("Digite a quantidade de faltas no mês: "))
bonus = input("Digite se recebeu bonus por desempenho: ").lower().strip()
valor_bonus = 0

valor_hora_extra = salario * 0.015 * horas_extras
desconto_falta = salario * 0.02 * faltas

if bonus == "s" or bonus == "sim":
    if cargo == "gerente":
        valor_bonus = 1000
    elif cargo == "analista":
        valor_bonus = 500
    elif cargo == "assistente":
        valor_bonus = 300
    elif cargo == "estagiário" or cargo == "estagiario":
        valor_bonus = 100
    else:
        print("cargo invalido")

salario_bruto = salario + valor_bonus + valor_hora_extra
total_acrescimos = valor_bonus + valor_hora_extra
salario_final = salario + valor_hora_extra + valor_bonus - desconto_falta

print(f"Seu salário bruto é: {salario_bruto}")
print(f"Seu total em acréscimos foi de: {total_acrescimos}  ")
print(f"Seu desconto foi de {desconto_falta}  ")
print(f"Seu salário final foi de: {salario_final}")