# Script de Visualização de Dados: (será usado para questões futuras)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Função para carregar os dados
def load_data(file_path):
    df = pd.read_excel(file_path)
    return df

# Função para visualizar os dados
def visualize_data(df):
    sns.set(style="whitegrid")

    # Gráfico de barras da contagem de bots vs humanos
    plt.figure(figsize=(10, 6))
    sns.countplot(x='is_a_bot', data=df)
    plt.title('Contagem de Bots vs Humanos')
    plt.xlabel('Bot')
    plt.ylabel('Contagem')
    plt.show()

    # Histogramas das features numéricas
    numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
    df[numerical_columns].hist(bins=15, figsize=(15, 10), layout=(5, 4))
    plt.suptitle('Distribuição das Features Numéricas')
    plt.show()

# Exemplo de execução do script
if __name__ == "__main__":
    df = load_data('twitter_bots.xlsx')
    visualize_data(df)
