import matplotlib.pyplot as plt

# Resultados das execuções para 10.000 vértices (sequencial)
execucoes_sequencial = [
    50.40,
    49.40,
    49.40,
    48.60,
    49.00,
    49.00,
    48.80,
    50.40,
    50.40,
    48.60
]

# Resultados das execuções para 10.000 vértices (1 thread)
execucoes_1_thread = [
    64.60,
    45.60,
    54.60,
    43.80,
    51.60,
    42.40,
    45.00,
    42.80,
    41.80,
    35.40
]

# Resultados das execuções para 10.000 vértices (2 threads)
execucoes_2_threads = [
    18.20,
    18.60,
    33.40,
    32.60,
    62.00,
    22.20,
    35.00,
    21.60,
    25.40,
    28.00
]

# Resultados das execuções para 10.000 vértices (3 threads)
execucoes_3_threads = [
    14.60,
    17.40,
    26.80,
    16.60,
    14.40,
    28.40,
    74.80,
    32.00,
    20.00,
    19.00
]

# Resultados das execuções para 10.000 vértices (4 threads)
execucoes_4_threads = [
    9.80,
    25.20,
    27.20,
    13.40,
    14.40,
    16.60,
    23.80,
    16.80,
    15.40,
    26.00
]

# Resultados das execuções para 10.000 vértices (5 threads)
execucoes_5_threads = [
    9.00,
    13.00,
    9.00,
    8.60,
    26.60,
    9.80,
    8.20,
    7.80,
    9.40,
    16.00
]

# Resultados das execuções para 10.000 vértices (6 threads)
execucoes_6_threads = [
    4.00,
    4.60,
    4.00,
    4.00,
    4.20,
    5.00,
    4.00,
    4.40,
    4.40,
    4.00
]

# Função para calcular a média
def calcular_media(execucoes):
    return sum(execucoes) / len(execucoes)

# Cálculo das médias
media_sequencial = calcular_media(execucoes_sequencial)
media_1_thread = calcular_media(execucoes_1_thread)
media_2_threads = calcular_media(execucoes_2_threads)
media_3_threads = calcular_media(execucoes_3_threads)
media_4_threads = calcular_media(execucoes_4_threads)
media_5_threads = calcular_media(execucoes_5_threads)
media_6_threads = calcular_media(execucoes_6_threads)

# Exibição dos resultados
print(f"Média do tempo de execução (sequencial) para 10.000 vértices: {media_sequencial:.2f} ms")
print(f"Média do tempo de execução (1 thread) para 10.000 vértices: {media_1_thread:.2f} ms")
print(f"Média do tempo de execução (2 threads) para 10.000 vértices: {media_2_threads:.2f} ms")
print(f"Média do tempo de execução (3 threads) para 10.000 vértices: {media_3_threads:.2f} ms")
print(f"Média do tempo de execução (4 threads) para 10.000 vértices: {media_4_threads:.2f} ms")
print(f"Média do tempo de execução (5 threads) para 10.000 vértices: {media_5_threads:.2f} ms")
print(f"Média do tempo de execução (6 threads) para 10.000 vértices: {media_6_threads:.2f} ms")

# Plotagem do gráfico de barras
num_threads = [1, 2, 3, 4, 5, 6]
medias = [media_1_thread, media_2_threads, media_3_threads, media_4_threads, media_5_threads, media_6_threads]
plt.bar(num_threads, medias)
plt.xlabel("Número de threads")
plt.ylabel("Tempo (ms)")
plt.title("Tempo médio de execução")

# Inserindo os valores no topo das barras
for i in range(len(num_threads)):
    plt.text(num_threads[i], medias[i], f"{medias[i]:.2f}", ha='center', va='bottom')

plt.show()