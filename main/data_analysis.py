import pandas as pd
import matplotlib.pyplot as plt


# Caminho do arquivo enviado
file_path = 'data/world_data.csv'

# Carregar os dados
data = pd.read_csv(file_path)
import matplotlib.pyplot as plt

# Verificar colunas relacionadas à expectativa de vida
data.columns

# Adaptar o gráfico usando a população acima de 65 anos como um possível indicador indireto
# Selecionar dados para 5 países específicos e anos mais recentes (adaptado)
selected_countries = ["Brazil", "United States", "India", "China", "Germany"]
line_chart_data = data[data['pais'].isin(selected_countries)][['ano', 'pais', 'populacao_acima_65']].dropna()

# Criar gráfico de linhas para esses países
plt.figure(figsize=(10, 6))
for country in selected_countries:
    country_data = line_chart_data[line_chart_data['pais'] == country]
    plt.plot(country_data['ano'], country_data['populacao_acima_65'], label=country)

# Configurações do gráfico
plt.title("Proporção da População Acima de 65 Anos (Indicador Indireto de Expectativa de Vida)", fontsize=14)
plt.xlabel("Ano", fontsize=12)
plt.ylabel("População acima de 65 anos (%)", fontsize=12)
plt.legend(title="País", fontsize=10)
plt.grid(visible=True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# Preparar dados para o box-plot: acesso à água potável por continente
boxplot_data = data[['continente', 'acesso_agua_potavel']].dropna()

# Criar box-plot
plt.figure(figsize=(10, 6))
boxplot_data.boxplot(by='continente', column='acesso_agua_potavel', grid=False, patch_artist=True,
                     boxprops=dict(facecolor='lightblue', color='blue'),
                     medianprops=dict(color='red', linewidth=2),
                     showfliers=True)

# Configurações do gráfico
plt.title("Acesso à Água Potável por Continente", fontsize=14)
plt.suptitle("")  # Remover título automático do boxplot
plt.xlabel("Continente", fontsize=12)
plt.ylabel("Proporção de acesso à água potável (%)", fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# Preparar dados para o gráfico de linhas: crescimento médio populacional por continente
growth_data = data[['ano', 'continente', 'crescimento_populacao']].dropna()
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