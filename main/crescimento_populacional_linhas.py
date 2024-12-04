import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo enviado
file_path = 'data/world_data.csv'

# Carregar os dados
data = pd.read_csv(file_path)

# Ajustar nomes de continentes para unificar
data['continente'] = data['continente'].replace({
    'North America': 'America',
    'South America': 'America',
    'Australasia': 'Oceania',
    'Central America': 'America',
    'Europe & Central Asia': 'Europe',
    'East Asia & Pacific': 'Asia',
    'Sub-Saharan Africa': 'Africa'
})

# Filtrar os seis principais continentes
main_continents = ['Africa', 'America', 'Asia', 'Europe', 'Oceania', 'Antarctica']
filtered_data = data[data['continente'].isin(main_continents)]

# Preparar dados para o gráfico de linhas: crescimento médio populacional por continente
growth_data = filtered_data[['ano', 'continente', 'crescimento_populacao']].dropna()
mean_growth_per_continent = growth_data.groupby(['ano', 'continente']).mean().reset_index()

# Criar gráfico de linhas para cada continente
plt.figure(figsize=(12, 6))
for continent in mean_growth_per_continent['continente'].unique():
    continent_data = mean_growth_per_continent[mean_growth_per_continent['continente'] == continent]
    plt.plot(continent_data['ano'], continent_data['crescimento_populacao'], label=continent)

# Configurações do gráfico
plt.title("Evolução do Crescimento Médio Populacional por Continente", fontsize=14)
plt.xlabel("Ano", fontsize=12)
plt.ylabel("Taxa de Crescimento Populacional (%)", fontsize=12)
plt.legend(title="Continente", fontsize=10)
plt.grid(visible=True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
