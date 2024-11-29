import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo enviado
file_path = 'data/world_data.csv'

# Carregar os dados
data = pd.read_csv(file_path)

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