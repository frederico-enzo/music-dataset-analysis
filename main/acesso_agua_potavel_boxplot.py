import os
import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo enviado
file_path = 'data/world_data.csv'

# Carregar os dados
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

# Filtrar os seis principais continentes (incluindo Antártida)
main_continents = ['Africa', 'America', 'Asia', 'Europe', 'Oceania', 'Antarctica']
filtered_data = data[data['continente'].isin(main_continents)]

# Preparar dados para o box-plot: acesso à água potável por continente
boxplot_data = filtered_data[['continente', 'acesso_agua_potavel']].dropna()

# Criar box-plot sem outliers
plt.figure(figsize=(10, 6))
boxplot_data.boxplot(by='continente', column='acesso_agua_potavel', grid=False, patch_artist=True,
                     boxprops=dict(facecolor='lightblue', color='blue'),
                     medianprops=dict(color='red', linewidth=2),
                     showfliers=False)  # Remover os outliers

# Configurações do gráfico
plt.title("Acesso à Água Potável por Continente", fontsize=14)
plt.suptitle("")  # Remover título automático do boxplot
plt.xlabel("Continente", fontsize=12)
plt.ylabel("Proporção de acesso à água potável (%)", fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.8)
# Salvar o gráfico em um arquivo PNG
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "acesso_agua_potavel_boxplot.png"))

plt.show()

