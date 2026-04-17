# Funções
def calcular_horas_extras(salario_base, horas):
    return salario_base * 0.015 * horas

def calcular_descontos_faltas(salario_base, faltas):
    return salario_base * 0.02 * faltas

def calcular_bonus(cargo, recebeu_bonus):
    match recebeu_bonus:
        case "s":
            match cargo:
                case 1:
                    return 1000
                case 2:
                    return 500
                case 3:
                    return 300
                case 4:
                    return 100
        case "n":
            return 0

def calcular_salario_bruto(salario, bonus, valor_hora):
    return salario + bonus + valor_hora

def calcular_acrescimos(bonus, valor_hora):
    return bonus + valor_hora

def calcular_salario_final(salario_bruto, desconto_faltas):
    return salario_bruto - desconto_faltas

print("Cálculo do salário final")

nome = input("Digite seu nome: ")
cargo = int(input("--- CARGOS ---\n1-Gerente\n2-Analista\n3-Assistente\n4-Estagiário\nDigite seu cargo: "))
salario = float(input("Digite seu salario base: "))
horas_extras = int(input("Digite a quantidade de horas extras trabalhadas: "))
faltas = int(input("Digite a quantidade de faltas no mês: "))
bonus = input("Digite se recebeu bonus por desempenho (s ou n): ")

valor_hora_extra = calcular_horas_extras(salario, horas_extras)
desconto_falta = calcular_descontos_faltas(salario, faltas)
valor_bonus = calcular_bonus(cargo, bonus)

salario_bruto = calcular_salario_bruto(salario, valor_bonus, valor_hora_extra)
total_acrescimos = calcular_acrescimos(valor_bonus, valor_hora_extra)
salario_final = calcular_salario_final(salario_bruto, desconto_falta)

print(f"Seu salário bruto é: R$ {salario_bruto:.2f}")
print(f"Seu total em acréscimos foi de: R$ {total_acrescimos:.2f}")
print(f"Seu desconto foi de: R$ {desconto_falta:.2f}")
print(f"Seu salário final foi de: R$ {salario_final:.2f}")