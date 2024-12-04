import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
file_path = 'data/world_data.csv'
data = pd.read_csv(file_path)

# Criar a pasta "graficos" se não existir
output_dir = "graficos"
os.makedirs(output_dir, exist_ok=True)

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

# Ajustar estilo do gráfico para paleta acessível
sns.set(style="whitegrid", palette="muted")

# Definir a fonte para uma mais agradável
plt.rcParams["font.family"] = "Verdana"  # Substitua por uma fonte que você prefira

# Criar o gráfico com facetas por continente
plt.figure(figsize=(15, 8))  # Aumentando a altura para melhorar a visibilidade
g = sns.FacetGrid(filtered_data, col='continente', col_wrap=3, height=4, sharex=False, sharey=False)

# Plotar o histograma de crescimento da população em cada faceta
g.map(sns.histplot, 'crescimento_populacao', kde=True, color='mediumseagreen', bins=15)

# Adicionar linha de média em todas as facetas
for ax in g.axes.flat:
    # Calcular a média do crescimento da população para cada faceta
    mean_value = filtered_data['crescimento_populacao'].mean()
    # Adicionar a linha de média
    ax.axvline(mean_value, color='red', linestyle='--', label=f'Média: {mean_value:.2f}%')
    ax.legend()
   
# Ajustar títulos e rótulos
g.set_axis_labels('Crescimento da População (%)', fontsize=10)
g.set_titles('{col_name}', fontsize=14, fontweight='bold')
g.fig.suptitle('Distribuição do Crescimento da População por Continente', fontsize=16, y=1.03, fontweight='bold')

# Adicionar manualmente os rótulos para as facetas 'Asia' e 'Europe' 
for ax in g.axes.flat:
    ax.set_xlabel('Crescimento da População (%)', fontsize=12, fontweight='bold')

# Melhorar a visibilidade da grade, destacando o eixo Y
plt.grid(visible=True, linestyle='--', alpha=0.7, linewidth=0.7)

# Ajustar o layout para garantir boa visibilidade dos rótulos e legendas
plt.subplots_adjust(hspace=0.4, top=0.93)  # Ajustando hspace e o topo para evitar sobreposição
plt.savefig(os.path.join(output_dir, "crescimento_populacao_por_continente.png"))

# Exibir o gráfico
plt.show()
