import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import random
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
from pgmpy.parameter_estimator import DiscreteMLE

def visualizar_rede(modelo, titulo="Rede Bayesiana"):
    plt.figure(figsize=(10, 6))
    pos = nx.circular_layout(modelo)
    nx.draw_networkx_nodes(modelo, pos, node_color='lightblue', node_size=2200)
    nx.draw_networkx_edges(modelo, pos, edge_color='gray', arrows=True,arrowstyle='-|>', arrowsize=20, node_size=2200)
    nx.draw_networkx_labels(modelo, pos, font_size=12, font_weight='bold')
    plt.title(titulo, fontsize=16, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(titulo)

ESTADOS = ['Nao', 'Sim']
ESTADOS_SATURACAO = ['Normal', 'Reduzida', 'Critica']
ESTADOS_PRESSAO = ['Normal', 'Baixa']
ESTADOS_IDADE = ['Crianca', 'Adulto', 'Idoso']
ESTADOS_GRAVIDADE = ['Baixa', 'Media', 'Alta']
ESTADO_RISCO = ['Baixa', 'Media', 'Alta']


n_pacientes = 2000
def gerar_paciente():

    febre = random.choices(
        ESTADOS,
        weights=[0.7,0.3]
    )[0]

    saturacao = random.choices(
        ESTADOS_SATURACAO,
        weights=[0.72,0.22,0.06]
    )[0]

    pressao = random.choices(
        ESTADOS_PRESSAO,
        weights=[0.82,0.18]
    )[0]

    idade = random.choices(
        ESTADOS_IDADE,
        weights=[0.20,0.60,0.20]
    )[0]

    doenca = random.choices(
        ESTADOS,
        weights=[0.72,0.28]
    )[0]


    score = 0

    if febre == "Sim":
        score += 1

    if saturacao == "Reduzida":
        score += 2

    elif saturacao == "Critica":
        score += 5

    if pressao == "Baixa":
        score += 3

    if idade == "Idoso":
        score += 1

    if doenca == "Sim":
        score += 1


    if score <= 2:

        gravidade = random.choices(
            ["Baixa","Media","Alta"],
            weights=[0.85,0.10, 0.05]
        )[0]

    elif score <= 5:

        gravidade = random.choices(
            ["Baixa","Media","Alta"],
            weights=[0.15,0.75,0.10]
        )[0]

    else:

        gravidade = random.choices(
            ["Baixa","Media","Alta"],
            weights=[0.05, 0.10,0.85]
        )[0]

    score_risco = 0

    if gravidade == "Media":
        score_risco += 2

    elif gravidade == "Alta":
        score_risco += 5

    if idade == "Idoso":
        score_risco += 2

    if doenca == "Sim":
        score_risco += 2

    if saturacao == "Critica":
        score_risco += 3

    elif saturacao == "Reduzida":
        score_risco += 1


    if score_risco <= 2:

        risco = random.choices(
            ["Baixa","Media"],
            weights=[0.96,0.04]
        )[0]

    elif score_risco <= 5:

        risco = random.choices(
            ["Baixa","Media","Alta"],
            weights=[0.15,0.75,0.10]
        )[0]

    else:

        risco = random.choices(
            ["Media","Alta"],
            weights=[0.08,0.92]
        )[0]


    return {
        "Febre": febre,
        "Saturacao_O2": saturacao,
        "Pressao_Arterial": pressao,
        "Idade": idade,
        "Doenca_Cronica": doenca,
        "Gravidade": gravidade,
        "Risco_Deterioracao": risco
    }

dados = [gerar_paciente() for _ in range(n_pacientes)]

df = pd.DataFrame(dados)


modelo_triagem = DiscreteBayesianNetwork([
    ['Febre', 'Gravidade'],
    ['Saturacao_O2', 'Gravidade'],
    ['Pressao_Arterial', 'Gravidade'],
    ['Idade', 'Risco_Deterioracao'],
    ['Doenca_Cronica', 'Risco_Deterioracao'],
    ['Gravidade', 'Risco_Deterioracao']
])

modelo_triagem.fit(df, estimator=DiscreteMLE())


if __name__ == '__main__':
    print("Nós:\n", modelo_triagem.nodes(),'\n')
    print("Arestas:\n", modelo_triagem.edges(),'\n')
    visualizar_rede(modelo_triagem)

    print("CPT DA FEBRE")
    print(modelo_triagem.get_cpds('Febre'))

    print("\nCPT DA SATURAÇÃO")
    print(modelo_triagem.get_cpds('Saturacao_O2'))

    print("\nCPT DA PRESSÃO")
    print(modelo_triagem.get_cpds('Pressao_Arterial'))

    print("\nCPT DA IDADE")
    print(modelo_triagem.get_cpds('Idade'))

    print("\nCPT DA DOENÇA CRÔNICA")
    print(modelo_triagem.get_cpds('Doenca_Cronica'))

    print("\nCPT DA GRAVIDADE")
    print(modelo_triagem.get_cpds('Gravidade'))

    print("\nCPT DO RISCO DE DETERIORAÇÃO")
    print(modelo_triagem.get_cpds('Risco_Deterioracao'))

    print("Modelo ok: ")
    print(modelo_triagem.check_model())

inferencia = VariableElimination(modelo_triagem)

