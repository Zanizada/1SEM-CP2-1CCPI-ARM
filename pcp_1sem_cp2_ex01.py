def conversao_carga_t(carga):
    return carga / 1000

def precos_carga(codigo):
    if 10 <= codigo <= 20:
        return 100.00
    elif 21 <= codigo <= 30:
        return 250.00
    elif 31 <= codigo <= 40:
        return 340.00

def calculo_preco(carga, preco):
    return carga * preco

def imposto_cobrado(valor, imposto):
    return valor*imposto

def valor_total(valor, imposto):
    return valor - (imposto_cobrado(valor, imposto))

impostos = {
    1: 0.35,
    2: 0.25,
    3: 0.15,
    4: 0.05,
    5: 0.00,
}

codigo_estado = int(input("Digite o código do estado (1 a 5): "))
peso_carga = float(input("Digite o peso da carga do caminhão: "))
codigo_carga = int(input("Digite o código da carga (10 a 40): "))
valor = calculo_preco(peso_carga, precos_carga(codigo_carga))

print(f"Quantidade da carga em Toneladas: {conversao_carga_t(peso_carga):.1f}T")
print(f"Preço da carga: R$ {valor:.2f}")
print(f"Porcentagem de imposto: {impostos[codigo_estado]*100:.0f}%")
print(f"Imposto cobrado: R$ {imposto_cobrado(valor, impostos[codigo_estado]):.2f}")
print(f"Valor total: R$ {valor_total(valor, impostos[codigo_estado]):.2f}")