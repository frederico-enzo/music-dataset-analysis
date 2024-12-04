import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # Para paletas de cores melhores

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

# Definir uma paleta de cores agradável e contrastante
sns.set_palette("Set2")  # Paleta acessível e equilibrada

# Criar gráfico de linhas para cada continente
plt.figure(figsize=(12, 6))
for continent in mean_growth_per_continent['continente'].unique():
    continent_data = mean_growth_per_continent[mean_growth_per_continent['continente'] == continent]
    plt.plot(continent_data['ano'], continent_data['crescimento_populacao'], label=continent,
             linewidth=2, marker='o', markersize=6)  # Adicionando marcadores nos pontos de ano

# Configurações do gráfico
plt.title("Evolução do Crescimento Médio Populacional por Continente", fontsize=16, fontweight='bold')
plt.xlabel("Ano", fontsize=14)
plt.ylabel("Taxa de Crescimento Populacional (%)", fontsize=14)

# Melhorar a visibilidade da grade
plt.grid(visible=True, linestyle='--',  alpha=0.7, linewidth=1.0)  # Ajuste de opacidade e espessura

# Ajustar os ticks do eixo Y para um intervalo mais adequado
plt.yticks(range(-0, 4, 1))  # Ajuste de intervalo para o eixo Y

# Ajustar a exibição do eixo X para todos os anos
plt.xticks(ticks=sorted(mean_growth_per_continent['ano'].unique()), rotation=45, fontsize=12)

# Adicionar legenda e ajustar posição
plt.legend(title="Continente", fontsize=12, loc='upper left', bbox_to_anchor=(1, 1))

# Ajustar layout para melhor visibilidade
plt.tight_layout()

# Mostrar o gráfico
plt.show()
