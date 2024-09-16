import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Exemplo de criação de DataFrame para logs simulados de ambiente de testes
data = {
    'timestamp': ['2024-09-13 08:45:00', '2024-09-13 08:46:00', '2024-09-13 08:47:00'],
    'evento': ['Login', 'Erro de Conexão', 'Logout'],
    'servidor': ['Teste 1', 'Teste 2', 'Teste 1']
}

df = pd.DataFrame(data)
print(df)

# Preparação de dados: preenchendo valores nulos em logs de testes
df['evento'] = df['evento'].fillna('Desconhecido')
print(df)

# Filtrando logs de erros de conexão em ambiente de testes
erros_conexao = df[df['evento'] == 'Erro de Conexão']
print(erros_conexao)

# Contando eventos por servidor de teste
eventos_por_servidor = df.groupby('servidor').count()
print(eventos_por_servidor)

# Gráfico de eventos por servidor de teste
sns.countplot(data=df, x='servidor', hue='evento')
plt.title('Eventos por Servidor de Teste')
plt.show()

