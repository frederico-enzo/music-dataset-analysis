import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
file_path = 'data/world_data.csv'
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

# Ajustar estilo do gráfico
sns.set(style="whitegrid")

# Criar o gráfico com facetas por continente
plt.figure(figsize=(16, 10))
g = sns.FacetGrid(filtered_data, col='continente', col_wrap=3, height=4, sharex=False, sharey=False)

# Plotar o histograma de crescimento da população em cada faceta
g.map(sns.histplot, 'crescimento_populacao', kde=True, color='skyblue')

# Ajustar títulos e rótulos
g.set_axis_labels('Crescimento da População (%)', fontsize=12)
g.set_titles('{col_name}', fontsize=14)
g.fig.suptitle('Distribuição do Crescimento da População por Continente', fontsize=16, y=1.03)

# Ajustar layout para melhor visibilidade
plt.tight_layout()
plt.show()
