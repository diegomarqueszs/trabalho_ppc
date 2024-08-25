# Plota um gráfico comparativo entre os dois algoritmos com intervalo de confiança de 95%
# É utilizado a execução com 3 threads do algoritmo paralelo

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

# Dados do algoritmo sequencial
data_nao_paralelo = [
    [1000, 0.00, 0.00, 0.00, 0.20, 0.20, 0.00, 0.00, 0.00, 0.20],
    [2000, 2.20, 2.00, 2.00, 2.00, 2.20, 2.00, 2.00, 2.20, 2.20],
    [3000, 4.80, 4.20, 4.20, 5.00, 4.80, 4.60, 4.20, 4.00, 4.40],
    [4000, 8.20, 8.80, 7.80, 8.20, 8.20, 8.40, 7.60, 7.60, 7.80],
    [5000, 13.20, 12.40, 12.40, 12.20, 12.00, 12.20, 13.40, 12.20, 12.40],
    [6000, 18.40, 17.60, 17.40, 17.60, 17.40, 18.00, 18.20, 18.00, 17.20],
    [7000, 24.00, 24.00, 24.40, 24.20, 25.60, 23.80, 25.60, 24.00, 23.80],
    [8000, 31.40, 32.00, 31.20, 32.20, 31.40, 31.60, 32.00, 31.40, 31.20],
    [9000, 39.20, 41.00, 39.60, 40.20, 40.60, 40.40, 39.80, 39.60, 39.00],
    [10000, 50.40, 49.40, 49.40, 48.60, 49.00, 49.00, 48.80, 50.40, 48.60],
]

# Dados do algoritmo paralelo
data_paralelo = [
    [1000, 0.40, 1.00, 1.60, 1.00, 0.60, 0.60, 2.80, 1.00, 0.40, 1.00],
    [2000, 3.40, 1.40, 5.00, 2.20, 2.80, 1.80, 7.40, 8.60, 3.60, 2.60],
    [3000, 4.40, 2.20, 3.00, 15.80, 2.80, 5.60, 9.40, 7.00, 2.80, 2.80],
    [4000, 4.80, 3.20, 9.40, 15.00, 8.00, 3.60, 18.20, 12.40, 2.60, 4.00],
    [5000, 9.00, 4.40, 5.00, 16.00, 5.20, 6.20, 29.40, 44.20, 3.60, 7.00],
    [6000, 7.40, 6.20, 8.20, 9.40, 6.40, 7.80, 26.60, 67.60, 7.20, 6.40],
    [7000, 11.40, 9.20, 9.40, 16.00, 9.80, 11.00, 15.20, 47.80, 8.40, 6.60],
    [8000, 13.00, 10.20, 10.00, 30.00, 15.80, 15.40, 26.40, 33.20, 11.00, 10.40],
    [9000, 14.60, 34.80, 29.80, 14.20, 49.80, 26.20, 25.20, 57.00, 17.40, 16.80],
    [10000, 14.60, 17.40, 26.80, 16.60, 14.40, 28.40, 74.80, 32.00, 20.00, 19.00],
]

# Função para calcular média e intervalo de confiança de 95%
def calc_stats(data):
    means = np.mean(data, axis=1)
    ci = st.t.interval(0.95, len(data[0])-1, loc=means, scale=st.sem(data, axis=1))
    return means, ci

# Extraindo médias e intervalos de confiança
means_nao_paralelo, ci_nao_paralelo = calc_stats(np.array([x[1:] for x in data_nao_paralelo]))
means_paralelo, ci_paralelo = calc_stats(np.array([x[1:] for x in data_paralelo]))

# Gráfico
vertices = [x[0] for x in data_nao_paralelo]

plt.figure(figsize=(10, 6))
plt.plot(vertices, means_nao_paralelo, label='Sequencial', color='blue', marker='o')
plt.fill_between(vertices, ci_nao_paralelo[0], ci_nao_paralelo[1], color='blue', alpha=0.2)

plt.plot(vertices, means_paralelo, label='Paralelo', color='red', marker='o')
plt.fill_between(vertices, ci_paralelo[0], ci_paralelo[1], color='red', alpha=0.2)

plt.xlabel('Número de Vértices')
plt.ylabel('Tempo de Execução (ms)')
plt.title('Paralelo ( 3 threads ) vs Sequencial')
plt.legend()
plt.grid(True)
plt.show()
