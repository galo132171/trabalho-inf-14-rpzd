# Tabela de carros - nota de 0 a 10 (desempenho, economia, manutenção, conforto)
carros = {
    "Dodge RAM": {"desempenho": 10, "economia": 3, "manutencao": 4, "conforto": 9},
    "Civic": {"desempenho": 7, "economia": 8, "manutencao": 8, "conforto": 8},
    "Pálio": {"desempenho": 4, "economia": 10, "manutencao": 9, "conforto": 5},
    "Ferrari": {"desempenho": 10, "economia": 1, "manutencao": 2, "conforto": 10}
}

print("=== COMPARADOR DE CUSTO-BENEFÍCIO ===\n")

# Pessoa digita o preço de cada carro
precos = {}
for nome in carros:
    while True:
        try:
            valor = float(input(f"Digite o preço da {nome} R$: "))
            precos[nome] = valor
            break
        except:
            print("Digite só número. Ex: 85000")

print("\n--- RESULTADO ---\n")

resultados = []

for nome, notas in carros.items():
    # Calcula média das notas
    media_notas = sum(notas.values()) / len(notas)
    preco = precos[nome]

    # Custo-benefício = (média de notas * 10000) / preço
    # Quanto MAIOR o número, melhor o custo-benefício
    custo_beneficio = (media_notas * 10000) / preco

    resultados.append({
        "nome": nome,
        "preco": preco,
        "media": media_notas,
        "cb": custo_beneficio
    })

    print(f"{nome}")
    print(f" Preço: R$ {preco:,.2f}")
    print(f" Nota média: {media_notas:.1f}/10")
    print(f" Custo-Benefício: {custo_beneficio:.4f}\n")

# Ordena do melhor para o pior custo-benefício
resultados.sort(key=lambda x: x["cb"], reverse=True)

print("=== RANKING DE CUSTO-BENEFÍCIO ===")
for i, r in enumerate(resultados, 1):
    print(f"{i}º - {r['nome']} (CB: {r['cb']:.4f})")

melhor = resultados[0]
print(f"\n>>> MELHOR ESCOLHA: {melhor['nome']} <<<")
print(f"Motivo: Maior nota pelo menor preço.")

# Recomendação extra
if melhor["nome"] == "Pálio":
    print("Recomendado para economia no dia a dia.")
elif melhor["nome"] == "Civic":
    print("Recomendado para equilíbrio entre tudo.")
elif melhor["nome"] == "Dodge RAM":
    print("Recomendado para força e conforto, se o preço compensar.")
else:
    print("Recomendado se o foco é desempenho e status, não economia.")
