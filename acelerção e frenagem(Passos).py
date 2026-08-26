# Dicionário com chaves em minúsculo para facilitar a busca
carros = {
    "dodge ram": {"nome": "Dodge Ram", "aceleracao": 5.0, "frenagem": 7.0},
    "civic": {"nome": "Honda Civic", "aceleracao": 6.5, "frenagem": 9.0},
    "palio": {"nome": "Fiat Palio", "aceleracao": 2.0, "frenagem": 6.0},
    "ferrari": {"nome": "Ferrari", "aceleracao": 10.0, "frenagem": 13.0}
}

# Tratamento da entrada: .strip() remove espaços extras e .lower() padroniza para minúsculas
entrada = input("Escolha o carro (ex: Dodge Ram, Civic, Palio, Ferrari): ").strip().lower()

if entrada in carros:
    dados = carros[entrada]
    aceleracao = dados["aceleracao"]
    frenagem = dados["frenagem"]
    
    # Cálculo: (100 km/h / 3.6) obtém a velocidade em m/s e divide pela aceleração
    tempo_0_100 = (100 / 3.6) / aceleracao

    print(f"\n--- {dados['nome']} ---")
    print(f"Aceleração: {aceleracao} m/s²")
    print(f"Frenagem: {frenagem} m/s²")
    print(f"Tempo de 0 a 100 km/h: {tempo_0_100:.2f} segundos")
else:
    print("\nCarro não encontrado! Verifique a digitação e tente novamente.")
