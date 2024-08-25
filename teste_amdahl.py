import numpy as np
import matplotlib.pyplot as plt

# Dados das execuções
execucoes_sequencial = [
    50.40, 49.40, 49.40, 48.60, 49.00, 49.00, 48.80, 50.40, 50.40, 48.60
]
execucoes_1_thread = [
    64.60, 45.60, 54.60, 43.80, 51.60, 42.40, 45.00, 42.80, 41.80, 35.40
]
execucoes_2_threads = [
    18.20, 18.60, 33.40, 32.60, 62.00, 22.20, 35.00, 21.60, 25.40, 28.00
]
execucoes_3_threads = [
    14.60, 17.40, 26.80, 16.60, 14.40, 28.40, 74.80, 32.00, 20.00, 19.00
]
execucoes_4_threads = [
    9.80, 25.20, 27.20, 13.40, 14.40, 16.60, 23.80, 16.80, 15.40, 26.00
]
execucoes_5_threads = [
    9.00, 13.00, 9.00, 8.60, 26.60, 9.80, 8.20, 7.80, 9.40, 16.00
]
execucoes_6_threads = [
    4.00, 4.60, 4.00, 4.00, 4.20, 5.00, 4.00, 4.40, 4.40, 4.00
]

# Calcular médias das execuções
def calcular_media(execucoes):
    return np.mean(execucoes)

tempo_sequencial = calcular_media(execucoes_sequencial)
tempos_threads = [
    calcular_media(execucoes_1_thread),
    calcular_media(execucoes_2_threads),
    calcular_media(execucoes_3_threads),
    calcular_media(execucoes_4_threads),
    calcular_media(execucoes_5_threads),
    calcular_media(execucoes_6_threads)
]

# Calcular speedup real
speedup_real = [tempo_sequencial / t for t in tempos_threads]

# Fração do tempo sequencial e speedup esperado
frac_sequencial = (tempos_threads[0] - tempos_threads[-1]) / tempos_threads[0]
speedup_esperado = [1 / ((1 - frac_sequencial) + (frac_sequencial / (i + 1))) for i in range(6)]

# Plotar gráficos
threads = [1, 2, 3, 4, 5, 6]

plt.figure(figsize=(12, 6))

# Speedup real
plt.subplot(1, 2, 1)
plt.plot(threads, speedup_real, 'bo-', label='Speedup Real')
plt.xlabel('Número de Threads')
plt.ylabel('Speedup')
plt.title('Speedup Real vs. Número de Threads')
plt.legend()

# Speedup esperado
plt.subplot(1, 2, 2)
plt.plot(threads, speedup_esperado, 'ro-', label='Speedup Esperado (Lei de Amdahl)')
plt.xlabel('Número de Threads')
plt.ylabel('Speedup')
plt.title('Speedup Esperado vs. Número de Threads')
plt.legend()

plt.tight_layout()
plt.show()
