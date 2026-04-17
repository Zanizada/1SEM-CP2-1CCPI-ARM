# Funções
def encontrar_menor(nota1, nota2, nota3):
    menor = nota1
    if nota2 < menor:
        menor = nota2
    if nota3 < menor:
        menor = nota3
    return menor

def calculo_media_semestre(nota1, nota2, nota3, nota_sp1, nota_sp2, nota_gs):
    menor = encontrar_menor(nota1, nota2, nota3)
    # A fórmula utiliza: (soma dos 2 maiores CPs + soma das 2 Sprints) / 4
    media_atividades = (nota1 + nota2 + nota3 - menor + nota_sp1 + nota_sp2) / 4
    return (media_atividades * 0.4) + (nota_gs * 0.6)

def calculo_media_peso(media):
    return media * 0.4

# 1 Solicitar notas
cp1 = float(input("Nota do Checkpoint 1: "))
cp2 = float(input("Nota do Checkpoint 2: "))
cp3 = float(input("Nota do Checkpoint 3: "))
sp1 = float(input("Nota da Sprint 1: "))
sp2 = float(input("Nota da Sprint 2: "))
gs = float(input("Nota da Global Solution: "))

# 2 Identificar menor nota entre os 3 checkpoints
menor = encontrar_menor(cp1, cp2, cp3)

# 3 Cálculo da média do semestre (sem peso)
media_semestre = calculo_media_semestre(cp1, cp2, cp3, sp1, sp2, gs)

# 4 Cálculo da média com peso 40%
media_peso = calculo_media_peso(media_semestre)

# 5 Resultado decimal
print(f"Menor nota de Checkpoint desconsiderada: {menor:.1f}")
print(f"Média do semestre (sem peso): {media_semestre:.1f}")
print(f"Média do semestre com peso (40%): {media_peso:.1f}")