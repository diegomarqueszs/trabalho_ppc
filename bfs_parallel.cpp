#include <iostream>
#include <vector>
#include <queue>
#include <omp.h>
#include <cstdlib>
#include <ctime>
#include <chrono>
#include <fstream>
#include <iomanip>

using namespace std;
using namespace std::chrono;

int V; 
vector<int> *adj;

// Inicializa o grafo com um número de vértices
void inicializarGrafo(int vertices) {
    V = vertices;
    adj = new vector<int>[V];
}

// Adiciona uma aresta entre dois vértices
void adicionarAresta(int v, int w) {
    adj[v].push_back(w);
    adj[w].push_back(v);
}

// Gera arestas aleatórias com base em uma probabilidade
void gerarArestasAleatorias(double probabilidadeAresta) {
    srand(time(0));
    for (int i = 0; i < V; ++i) {
        for (int j = i + 1; j < V; ++j) {
            if ((rand() / double(RAND_MAX)) < probabilidadeAresta) {
                adicionarAresta(i, j);
            }
        }
    }
}

// Realiza o algoritmo BFS de forma paralela
void bfsParalelo(int s) {
    bool *visitado = new bool[V];
    for (int i = 0; i < V; i++) {
        visitado[i] = false;
    }

    queue<int> q;
    visitado[s] = true;
    q.push(s);

    while (!q.empty()) {
        s = q.front();
        q.pop();

        // Inicia a região paralela onde cada thread irá trabalhar
        #pragma omp parallel
        {
            vector<int> local;

            // Cada thread verifica uma parte dos vizinhos de 's' de forma independente
            #pragma omp for nowait
            for (int i = 0; i < adj[s].size(); ++i) {
                int vizinho = adj[s][i];
                if (!visitado[vizinho]) {
                    
                    // A seção crítica garante que apenas uma thread por vez execute o bloco,
                    // para evitar que várias threads marquem o mesmo vizinho ao mesmo tempo
                    #pragma omp critical
                    {
                        if (!visitado[vizinho]) {
                            visitado[vizinho] = true;
                            local.push_back(vizinho);
                        }
                    }
                }
            }

            // Uma única thread adiciona os vizinhos encontrados à fila global
            #pragma omp single
            {
                for (int i : local) {
                    q.push(i);
                }
            }
        }
    }

    delete[] visitado;
}

int main() {
    ofstream arquivoSaida("tempos_bfs_paralela.txt");

    if (!arquivoSaida) {
        cerr << "Erro ao abrir arquivo para escrita." << endl;
        return 1;
    }

    double probabilidadeAresta = 0.05;
    int numIteracoes = 5;

    arquivoSaida << fixed << setprecision(2);

    for (int x = 0; x < 5; x++) {
        arquivoSaida << "Execução " << x << endl;
        for (int numVertices = 1000; numVertices <= 10000; numVertices += 1000) {
            long long duracaoTotal = 0;

            for (int i = 0; i < numIteracoes; ++i) {
                inicializarGrafo(numVertices);
                gerarArestasAleatorias(probabilidadeAresta);

                auto inicio = high_resolution_clock::now();
                bfsParalelo(0);
                auto fim = high_resolution_clock::now();
                auto duracao = duration_cast<milliseconds>(fim - inicio).count();
                duracaoTotal += duracao;
            }

            double duracaoMedia = static_cast<double>(duracaoTotal) / numIteracoes;
            arquivoSaida << "N vertices: " << numVertices << " -> " << duracaoMedia << " ms" << endl;
        }
        arquivoSaida << endl;
        cout << "Execução " << x << " - OK" << endl;
    }

    arquivoSaida.close();
    delete[] adj;
    return 0;
}
