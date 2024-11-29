import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo enviado
file_path = 'data/world_data.csv'

# Carregar os dados
data = pd.read_csv(file_path)
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