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
plt.figure(figsize=(12, 6))  # Ajustando o tamanho do gráfico para maior clareza
for country in selected_countries:
    country_data = line_chart_data[line_chart_data['pais'] == country]
    plt.plot(country_data['ano'], country_data['populacao_acima_65'], label=country, 
             linewidth=2, marker='o', markersize=6)  # Adicionando marcadores nos pontos de ano

# Melhorar escala e legibilidade
plt.title("Proporção da População Acima de 65 Anos (Indicador Indireto de Expectativa de Vida)", fontsize=16)
plt.xlabel("Ano", fontsize=14)
plt.ylabel("População Acima de 65 Anos (%)", fontsize=14)

# Ajustar o eixo y para uma escala mais adequada
plt.ylim(0, 40)  # Ajustar limite superior, dependendo dos dados

# Ajustar os ticks do eixo Y para 4 em 4
plt.yticks(range(0, 29, 4))  # De 0 até 40, com incremento de 4

# Ajustar a exibição do eixo X para todos os anos
plt.xticks(ticks=sorted(line_chart_data['ano'].unique()), rotation=45, fontsize=12)

# Adicionar legenda e ajustar posição
plt.legend(title="País", fontsize=12, loc='upper left')

# Melhorar a grade do gráfico com mais visibilidade
plt.grid(visible=True, linestyle='--', alpha=0.8, linewidth=1.5)  # Ajuste de alpha e linewidth

# Ajustar layout para melhor visibilidade
plt.tight_layout()
plt.show()
