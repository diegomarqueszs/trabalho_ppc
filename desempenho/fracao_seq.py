import matplotlib.pyplot as plt

# Calculadas manualmente com base na lei de amdahl e os speedups encontrados nos testes
fracoes_sequenciais = [ 100/100, 20/100, 30/100, 17/100, 4/100, -9/100]
num_threads = [1, 2, 3, 4, 5, 6]

# Plot
plt.plot(num_threads, fracoes_sequenciais, label='Fração Sequencial', color='green', marker='o')
plt.ylim(-0.2, 1.3)
plt.xlabel('Número de Threads')
plt.ylabel('Fração Sequencial')
plt.title('Fração Sequencial vs Número de Threads')
plt.legend()
plt.grid(True)

for i, j in zip(num_threads, fracoes_sequenciais):
    plt.text(i, j+0.03, f'{j*100:.2f}%', ha='center', va='bottom')

plt.show()