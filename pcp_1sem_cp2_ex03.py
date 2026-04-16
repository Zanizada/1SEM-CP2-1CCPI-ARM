# 1 Solicitar notas
cp1 = float(input("Nota do Checkpoint 1: "))
cp2 = float(input("Nota do Checkpoint 2: "))
cp3 = float(input("Nota do Checkpoint 3: "))
sp1 = float(input("Nota da Sprint 1: "))
sp2 = float(input("Nota da Sprint 2: "))
gs = float(input("Nota da Global Solution: "))

# 2 Identificar menor nota entre os 3 checkpoints
menor = cp1

if cp2 < menor:
    menor = cp2

if cp3 < menor:
    menor = cp3

# 3 Cálculo da média do semestre (sem peso)
# A fórmula utiliza: (soma dos 2 maiores CPs + soma das 2 Sprints) / 4
media_atividades = (cp1 + cp2 + cp3 - menor + sp1 + sp2) / 4
media_semestre = (media_atividades * 0.4) + (gs * 0.6)

# 4 Cálculo da média com peso 40%
media_peso = media_semestre * 0.4

# 5 Resultado decimal
print(f"Menor nota de Checkpoint desconsiderada: {menor:.1f}")
print(f"Média do semestre (sem peso): {media_semestre:.1f}")
print(f"Média do semestre com peso (40%): {media_peso:.1f}")