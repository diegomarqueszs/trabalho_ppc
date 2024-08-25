import matplotlib.pyplot as plt

# Números de vértices
vertices = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

# Valores de speedup correspondentes
speedup = [0.0577, 0.5361, 0.7957, 0.9951, 0.9585, 1.1580, 1.6823, 1.8005, 1.4010, 1.8712]

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(vertices, speedup, marker='o', linestyle='-', color='b')

# Títulos e rótulos
plt.title('Speedup vs Número de Vértices', fontsize=16)
plt.xlabel('Número de Vértices', fontsize=14)
plt.ylabel('Speedup', fontsize=14)
plt.grid(True)

# Exibindo o gráfico
plt.show()
