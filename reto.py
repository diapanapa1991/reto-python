import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Datos generados anteriormente
data = {
    'ID Cliente': [i for i in range(1, 101)],
    'Antigüedad (meses)': [12, 24, 6, 18, 8, 36, 14, 10, 22, 4,
                           30, 16, 20, 7, 26, 5, 15, 28, 9, 32,
                           11, 3, 14, 25, 13, 17, 21, 8, 19, 6,
                           14, 33, 12, 10, 25, 7, 18, 20, 9, 23,
                           15, 28, 11, 22, 5, 13, 16, 31, 8, 19,
                           7, 17, 23, 6, 15, 27, 13, 20, 8, 32,
                           11, 14, 18, 25, 7, 19, 9, 33, 16, 21,
                           12, 10, 28, 14, 23, 5, 17, 19, 8, 13,
                           26, 11, 30, 7, 22, 14, 16, 24, 9, 31,
                           12, 18, 5,10,15,5,23,45,6,1],
    'Facturación Promedio (USD)': [75, 120, 50, 90, 60, 150, 80, 70, 110, 40,
                                   130, 85, 100, 55, 125, 45, 78, 140, 65, 155,
                                   72, 35, 77, 118, 82, 88, 105, 62, 95, 48,
                                   79, 160, 76, 68, 115, 58, 92, 98, 67, 112,
                                   81, 145, 71, 42, 80, 87, 150, 63, 97, 54,
                                   122, 69, 84, 103, 73, 138, 66, 89, 114, 47,
                                   81, 132, 78, 99, 64, 158, 70, 76, 94, 120,
                                   56, 96, 68, 162, 86, 104, 77, 71, 142, 79,
                                   116, 43, 91, 101, 61, 79, 124, 74, 135, 53,
                                   110, 82, 88, 118, 66, 145, 72, 93, 46,55],
    'Segmento': ['Pymes', 'Postpago', 'Prepago', 'Postpago', 'Pymes',
                  'Postpago', 'Prepago', 'Pymes', 'Postpago', 'Prepago',
                  'Pymes', 'Postpago', 'Pymes', 'Prepago', 'Postpago',
                  'Prepago', 'Pymes', 'Postpago', 'Prepago', 'Pymes',
                  'Postpago', 'Prepago', 'Pymes', 'Postpago', 'Prepago',
                  'Pymes', 'Postpago', 'Prepago', 'Pymes', 'Prepago',
                  'Pymes', 'Postpago', 'Prepago', 'Pymes', 'Postpago',
                  'Prepago', 'Pymes', 'Postpago', 'Prepago', 'Pymes',
                  'Postpago', 'Prepago', 'Pymes', 'Prepago', 'Pymes',
                  'Postpago', 'Prepago', 'Pymes', 'Postpago', 'Pymes',
                  'Prepago', 'Postpago', 'Pymes', 'Prepago', 'Pymes',
                  'Postpago', 'Prepago', 'Pymes', 'Postpago', 'Prepago',
                  'Pymes', 'Postpago', 'Pymes', 'Prepago', 'Postpago',
                  'Pymes', 'Prepago', 'Pymes', 'Postpago', 'Prepago',
                  'Pymes', 'Postpago', 'Prepago', 'Pymes', 'Postpago',
                  'Prepago', 'Pymes', 'Postpago', 'Prepago','Prepago',
                  'Pymes', 'Postpago', 'Prepago','Prepago', 'Pymes',
                 'Postpago', 'Prepago','Prepago', 'Pymes', 'Postpago',
                 'Prepago','Postpago', 'Prepago','Prepago', 'Pymes',
                 'Postpago', 'Prepago', 'Pymes', 'Postpago', 'Prepago']
}
for key, value in data.items():
    print(f"{key}: {len(value)}")
# Creamos el dataframe
df = pd.DataFrame(data)
# Estadísticas descriptivas
desc_stats = df.describe()
print("Estadísticas Descriptivas:")
print(desc_stats)
# Histograma de la facturación promedio
plt.figure(figsize=(10, 6))
sns.histplot(df['Facturación Promedio (USD)'], bins=20, kde=True)
plt.title('Histograma de Facturación Promedio')
plt.xlabel('Facturación Promedio (USD)')
plt.ylabel('Frecuencia')
plt.show()
# Cálculo de correlación simple de campos numéricos
correlation_matrix = df.corr()
print("\nMatriz de Correlación:")
print(correlation_matrix)
# Gráfico de dispersión entre Antigüedad y Facturación Promedio
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Antigüedad (meses)', y='Facturación Promedio (USD)', data=df)
plt.title('Gráfico de Dispersión: Antigüedad vs. Facturación Promedio')
plt.xlabel('Antigüedad (meses)')
plt.ylabel('Facturación Promedio (USD)')
plt.show()
