import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# Exemplo de criação de DataFrame para logs simulados de ambiente de testes
data = {
    'timestamp': ['2024-09-13 08:45:00', '2024-09-13 08:46:00', '2024-09-13 08:47:00'],
    'evento': ['Login', 'Erro de Conexão', 'Logout'],
    'servidor': ['Teste 1', 'Teste 2', 'Teste 1']
}

df = pd.DataFrame(data)

# Preparação de dados: preenchendo valores nulos em logs de testes
df['evento'] = df['evento'].fillna('Desconhecido')


# Filtrando logs de erros de conexão em ambiente de testes
erros_conexao = df[df['evento'] == 'Erro de Conexão']

# Contando eventos por servidor de teste
eventos_por_servidor = df.groupby('servidor').size().reset_index(name='count')

# Gráfico de eventos por servidor de teste
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='servidor', hue='evento', palette='Set2')
plt.title('Eventos por Servidor de Teste', fontsize=14)
plt.xlabel('Servidor', fontsize=12)
plt.ylabel('Contagem de Eventos', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
