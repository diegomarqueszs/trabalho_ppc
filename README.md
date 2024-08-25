### Trabalho de Programação Paralela e Concorrente
- **Aluno**: Diego de Souza Marques
- **Aluno**: Maurício Martins Damasceno
- **Aluno**: Gabriel Fernando Zanda Gonçalves
- **Aluno**: Pedro Igor Ferreira Martins

### Descrição
Este trabalho tem como objetivo a implementação de uma BFS (Breadth First Search) em um grafo utilizando a linguagem de programação C++ e a biblioteca OpenMP. A BFS é um algoritmo de busca em largura que tem como objetivo percorrer todos os vértices de um grafo de forma iterativa, visitando todos os vértices vizinhos de um vértice de origem antes de avançar para os vértices vizinhos dos vértices visitados. O algoritmo é utilizado para encontrar o menor caminho entre dois vértices em um grafo não ponderado utilizando threads para paralelizar o processamento.

### Execução
```bash
top -H #Utilizado para visualizar a quantidade de threads abertas
```
#### BFS Serial
Para executar o algoritmo de BFS serial, basta executar o seguinte comando:
```bash
g++ -o bfs bfs.cpp 
./bfs
```

#### BFS Paralela
Para executar o algoritmo de BFS paralela, basta executar o seguinte comando:
```bash
g++ -fopenmp -o bfs_parallel bfs_parallel.cpp
./bfs_parallel
```

Caso deseje alterar o número de threads, basta usar a variável de ambiente `OMP_NUM_THREADS`:
```bash
export OMP_NUM_THREADS=4 # Altere para o número de threads desejado/suportado
```
