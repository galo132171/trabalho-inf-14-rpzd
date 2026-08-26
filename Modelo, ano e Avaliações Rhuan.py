import pandas as pd

# 1. Base de dados dos carros
dados_carros = {
    'Marca': ['Honda', 'RAM', 'Fiat', 'Ferrari'],
    'Modelo': ['Civic', 'Ram', 'Palio', 'Ferrari'],
    'Ano': [2022, 2023, 2016, 2020],
    'Avaliação (0-5)': [4.8, 4.6, 4.1, 4.9]
}

df_carros = pd.DataFrame(dados_carros)

# 2. Entrada do usuário
nome_busca = input("Digite o nome do carro (ex: Civic, Ram, Palio, Ferrari): ").strip()

# 3. Busca no DataFrame (ignorando maiúsculas e minúsculas)
resultado = df_carros[df_carros['Modelo'].str.lower() == nome_busca.lower()]

# 4. Exibição do resultado
if not resultado.empty:
    print("\nInformações encontradas:")
    display(resultado)
else:
    print(f"\nO carro '{nome_busca}' não foi encontrado na base de dados.")
