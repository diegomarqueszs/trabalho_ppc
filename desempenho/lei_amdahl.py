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

# Função para calcular o speedup esperado com base na Lei de Amdahl
def calcular_speedup_amdahl(num_threads):
    return 1 / ((1 - 0.83) + (0.83 / num_threads))

# Cálculo das médias
media_sequencial = calcular_media(execucoes_sequencial)
media_1_thread = calcular_media(execucoes_1_thread)
media_2_threads = calcular_media(execucoes_2_threads)
media_3_threads = calcular_media(execucoes_3_threads)
media_4_threads = calcular_media(execucoes_4_threads)
media_5_threads = calcular_media(execucoes_5_threads)
media_6_threads = calcular_media(execucoes_6_threads)

# Cálculo dos speedups reais
speedup_1_thread = media_sequencial / media_1_thread
speedup_2_threads = media_sequencial / media_2_threads
speedup_3_threads = media_sequencial / media_3_threads
speedup_4_threads = media_sequencial / media_4_threads
speedup_5_threads = media_sequencial / media_5_threads
speedup_6_threads = media_sequencial / media_6_threads

# Cálculo dos speedups esperados
speedup_1_thread_esperado = calcular_speedup_amdahl(1)
speedup_2_threads_esperado = calcular_speedup_amdahl(2)
speedup_3_threads_esperado = calcular_speedup_amdahl(3)
speedup_4_threads_esperado = calcular_speedup_amdahl(4)
speedup_5_threads_esperado = calcular_speedup_amdahl(5)
speedup_6_threads_esperado = calcular_speedup_amdahl(6)

print(f"\nSpeedup com 1 thread: {speedup_1_thread:.2f}")
print(f"Speedup com 2 threads: {speedup_2_threads:.2f}")
print(f"Speedup com 3 threads: {speedup_3_threads:.2f}")
print(f"Speedup com 4 threads: {speedup_4_threads:.2f}")
print(f"Speedup com 5 threads: {speedup_5_threads:.2f}")
print(f"Speedup com 6 threads: {speedup_6_threads:.2f}")

print(f"\nSpeedup esperado com 1 thread: {speedup_1_thread_esperado:.2f}")
print(f"Speedup esperado com 2 threads: {speedup_2_threads_esperado:.2f}")
print(f"Speedup esperado com 3 threads: {speedup_3_threads_esperado:.2f}")
print(f"Speedup esperado com 4 threads: {speedup_4_threads_esperado:.2f}")
print(f"Speedup esperado com 5 threads: {speedup_5_threads_esperado:.2f}")
print(f"Speedup esperado com 6 threads: {speedup_6_threads_esperado:.2f}")

# Plotando um gráfico de barras com os speedups reais e esperados
num_threads = [1, 2, 3, 4, 5, 6]
speedups_reais = [
    speedup_1_thread,
    speedup_2_threads,
    speedup_3_threads,
    speedup_4_threads,
    speedup_5_threads,
    speedup_6_threads,
]
speedups_esperados = [
    speedup_1_thread_esperado,
    speedup_2_threads_esperado,
    speedup_3_threads_esperado,
    speedup_4_threads_esperado,
    speedup_5_threads_esperado,
    speedup_6_threads_esperado,
]

plt.plot(num_threads, speedups_reais, label='Speedup Real', color='blue', marker='o')
plt.plot(num_threads, speedups_esperados, label='Speedup Amdahl', color='red', marker='o')
plt.xlabel('Número de Threads')
plt.ylabel('Speedup')
plt.title('Speedup Real vs Speedup Esperado')
plt.legend()
plt.grid(True)
plt.show()