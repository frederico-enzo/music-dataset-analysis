import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo enviado
file_path = 'data/world_data.csv'

# Carregar os dados
data = pd.read_csv(file_path)

# Filtrar dados apenas do Brasil
brazil_data = data[data['pais'] == 'Brazil']

# Selecionar as colunas relevantes
selected_columns = ['ano', 'populacao_acima_65', 'expec_vida']
filtered_brazil_data = brazil_data[selected_columns].dropna()

# Verificar se há dados suficientes
if filtered_brazil_data.empty:
    print("Não há dados suficientes para criar o gráfico de dispersão para o Brasil.")
else:
    # Criar gráfico de dispersão
    fig, ax1 = plt.subplots(figsize=(14, 7))

    # Plotar população acima de 65 anos como dispersão
    ax1.scatter(filtered_brazil_data['ano'], filtered_brazil_data['populacao_acima_65'], 
                color='#1f77b4', label='População Acima de 65 Anos (%)', s=120, alpha=0.8, edgecolors='black')

    # Criar um segundo eixo y para a expectativa de vida
    ax2 = ax1.twinx()
    ax2.plot(filtered_brazil_data['ano'], filtered_brazil_data['expec_vida'], 
             color='#d62728', marker='o', label='Expectativa de Vida (anos)', linewidth=2)

    # Adicionar títulos e rótulos
    ax1.set_xlabel('Ano', fontsize=14)
    ax1.set_ylabel('População Acima de 65 Anos (%)', fontsize=14, color='#1f77b4')
    ax2.set_ylabel('Expectativa de Vida (anos)', fontsize=14, color='#d62728')

    # Melhorar a legenda com posicionamento ajustado
    ax1.legend(loc='upper left', bbox_to_anchor=(0, 1.2), fontsize=12)
    ax2.legend(loc='upper right', bbox_to_anchor=(1, 1.2), fontsize=12)

    # Melhorar a grade e o layout
    plt.title('População Acima de 65 Anos e Expectativa de Vida no Brasil ao Longo dos Anos', fontsize=16)
    ax1.grid(visible=True, linestyle='--', alpha=0.9)

    # Ajustar layout para melhor visibilidade
    plt.tight_layout()

    # Exibir gráfico
    plt.show()
