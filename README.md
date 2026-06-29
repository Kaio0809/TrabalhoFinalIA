# Sistema Inteligente de Triagem Hospitalar com Rede Bayesiana e Busca A*

## Descrição

Este projeto implementa um sistema inteligente para priorização de pacientes em uma fila de atendimento hospitalar. A solução combina **Redes Bayesianas** para estimar o risco de deterioração clínica de cada paciente e o algoritmo de busca **A*** para determinar a ordem ótima de atendimento, buscando minimizar o risco acumulado de espera.

O sistema simula um ambiente de triagem em que cada paciente possui características clínicas, como febre, saturação de oxigênio, pressão arterial, idade e presença de doenças crônicas. A partir dessas informações, a Rede Bayesiana estima a probabilidade de deterioração clínica, que é utilizada pelo algoritmo A* para definir a sequência de atendimento.

---
# Autores

Projeto desenvolvido como parte da disciplina de Inteligência Artificial, utilizando Redes Bayesianas e Busca A* para apoio à decisão em sistemas de triagem hospitalar.
- Ana Riquele Geraldo Barroso - 557447
- Cauã de Freitas Souza - 554583
- Kaio Edmar Castro Barreto - 557246

---

# Objetivos

* Simular um processo de triagem hospitalar.
* Estimar o risco de deterioração clínica utilizando uma Rede Bayesiana.
* Encontrar a ordem de atendimento que minimize o risco associado ao tempo de espera.
* Comparar a estratégia inteligente com métodos tradicionais de atendimento, como FIFO.

---

# Tecnologias Utilizadas

* Python 3
* NumPy
* Pandas
* Matplotlib
* NetworkX
* pgmpy

---

# Estrutura do Projeto

```
.
├── rede_bayesiana.py      # Construção da Rede Bayesiana
├── busca_a_estrela.py     # Implementação do algoritmo A*
├── pacientes.py           # Definição dos pacientes
├── README.md
```

---

# Modelo Bayesiano

A Rede Bayesiana é composta pelas seguintes variáveis:

* Febre
* Saturação de Oxigênio
* Pressão Arterial
* Idade
* Doença Crônica
* Gravidade
* Risco de Deterioração

Estrutura da rede:

```
Febre --------------\
                     \
Saturação -----------> Gravidade --------\
                                          \
Pressão ------------/                      \
                                            ---> Risco de Deterioração
Idade ------------------------------------/
Doença Crônica ---------------------------/
```

---

# Geração dos Dados

Como não há acesso a uma base hospitalar real, o projeto utiliza um conjunto de dados sintéticos.

Os pacientes são gerados seguindo regras clínicas plausíveis, por exemplo:

* Saturação crítica aumenta significativamente a gravidade.
* Pressão arterial baixa aumenta a gravidade.
* Pacientes idosos apresentam maior risco.
* Pacientes com doenças crônicas possuem maior probabilidade de deterioração.
* Casos graves possuem maior chance de evoluir para alto risco.

Foi adicionada aleatoriedade durante a geração dos dados para que a Rede Bayesiana aprenda distribuições probabilísticas em vez de regras determinísticas.

---

# Algoritmo A*

Cada estado representa a fila atual de pacientes.

A função de custo considera:

* tempo de espera;
* probabilidade de deterioração clínica estimada pela Rede Bayesiana.

A heurística utilizada estima o custo futuro considerando o risco acumulado dos pacientes que ainda permanecem aguardando atendimento.

---

# Funcionamento

1. Geração da base sintética.
2. Treinamento da Rede Bayesiana.
3. Criação dos pacientes.
4. Inferência da probabilidade de deterioração para cada paciente.
5. Execução do algoritmo A*.
6. Retorno da ordem ótima de atendimento.

---

# Exemplo de Entrada

```python
Paciente(
    nome="Ana",
    sintomas={
        "Febre": "Sim",
        "Saturacao_O2": "Critica",
        "Pressao_Arterial": "Baixa",
        "Idade": "Idoso",
        "Doenca_Cronica": "Sim"
    }
)
```

---

# Exemplo de Saída

```
Pacientes:

Ana      P(Alta)=0.97
Bruno    P(Alta)=0.14
Carla    P(Alta)=0.56

Ordem ótima:

1. Ana
2. Carla
3. Bruno

Custo Total: 38.47
```

---

# Como Executar

Clone o repositório:

```bash
git clone <url-do-repositorio>
```

Instale as dependências:

```bash
pip install numpy pandas matplotlib networkx pgmpy
```

Execute a construção da Rede Bayesiana:

```bash
python rede_bayesiana.py
```

Em seguida execute o algoritmo de triagem:

```bash
python busca.py
```


