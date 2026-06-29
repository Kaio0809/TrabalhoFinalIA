import heapq
from IA.TrabalhoFinal.TrabalhoFinalIA.rede_beysiana import inferencia

class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __lt__(self, other):
        return self.path_cost < other.path_cost

    def __repr__(self):
        return f"<Node {self.state}>"

def calcular_probabilidade_risco(sintomas):
    try:
        resultado = inferencia.query(variables=['Risco_Deterioracao'], evidence=sintomas)
        
        prob_alta = resultado.values[resultado.get_state_no('Risco_Deterioracao', 'Alta')]
        return prob_alta
    except Exception as e:
        print(f"Erro na inferência: {e}")
        return 0.33


def solution(node):
    actions = []
    total_cost = node.path_cost
    curr = node
    while curr.parent is not None:
        actions.append(curr.action)
        curr = curr.parent
    return actions[::-1], total_cost

def expand(problem, node):
    s = node.state
    for action in problem.actions(s):
        s1, pac = problem.result(s, action)
        
        cost = node.path_cost + problem.action_cost(s)
        
        yield Node(state=s1, parent=node, action=action, path_cost=cost)


class Paciente:
    def __init__(self, nome, tempo_inicial_fila, sintomas):
        self.nome = nome
        self.tempo_inicial_fila = tempo_inicial_fila
        self.sintomas = sintomas
        self.prob_gravidade_alta = calcular_probabilidade_risco(sintomas)  

    def __repr__(self):
        return f"{self.nome} (P_Alta: {self.prob_gravidade_alta:.2f})"

class Triagem:
    def __init__(self, pacientes_iniciais):
        self.initial_state = (tuple(pacientes_iniciais), 0)
        self.tempo_atendimento = 10

    def is_goal(self, state):
        pacientes_restantes, _ = state
        return len(pacientes_restantes) == 0

    def actions(self, state):
        pacientes_restantes, _ = state
        return pacientes_restantes

    def result(self, state, action_paciente):
        pacientes_restantes, tempo_atual = state
        
        nova_fila = tuple(p for p in pacientes_restantes if p != action_paciente)
        novo_tempo = tempo_atual + self.tempo_atendimento
        
        return (nova_fila, novo_tempo), action_paciente

    def action_cost(self, state):
        pacientes_restantes, tempo_atual = state
        
        custo_passo = 0
        for p in pacientes_restantes:
            tempo_total_espera = p.tempo_inicial_fila + tempo_atual
            custo_passo += p.prob_gravidade_alta * tempo_total_espera
            
        return custo_passo


def heuristica_triagem(node):
    pacientes_restantes, tempo_atual = node.state
    
    h_custo = 0
    for paciente in pacientes_restantes:
        tempo_total_espera = paciente.tempo_inicial_fila + tempo_atual
        risco_atual = paciente.prob_gravidade_alta * tempo_total_espera
        h_custo += risco_atual
        
    return h_custo

def a_star_search(problem, h_func=heuristica_triagem):
    node = Node(problem.initial_state)
    frontier = []
    heapq.heappush(frontier, ((node.path_cost + h_func(node)), node))
    reached = {problem.initial_state: node}
    
    while frontier:
        priority, node = heapq.heappop(frontier)
        
        if problem.is_goal(node.state):
            return solution(node)
            
        for child in expand(problem, node):
            s = child.state
            if s not in reached or child.path_cost < reached[s].path_cost:
                reached[s] = child
                heapq.heappush(frontier, ((child.path_cost + h_func(child)), child))
                
    return None, float('inf')



if __name__ == "__main__":
    # Criando os pacientes do exemplo (Nome, Tempo de espera inicial, P(Gravidade Alta))

    # Criando os pacientes com seus respectivos quadros clínicos (Sintomas)
    # Os nomes das chaves e valores devem ser idênticos aos do DataFrame/Rede Bayesiana

    sintomas_ana = {
        'Febre': 'Sim',
        'Saturacao_O2': 'Critica',
        'Pressao_Arterial': 'Baixa',
        'Idade': 'Idoso',
        'Doenca_Cronica': 'Sim'
    }

    sintomas_bruno = {
        'Febre': 'Nao',
        'Saturacao_O2': 'Normal',
        'Pressao_Arterial': 'Normal',
        'Idade': 'Adulto',
        'Doenca_Cronica': 'Nao'
    }

    sintomas_carla = {
        'Febre': 'Sim',
        'Saturacao_O2': 'Reduzida',
        'Pressao_Arterial': 'Normal',
        'Idade': 'Crianca',
        'Doenca_Cronica': 'Nao'
    }

    # Instanciando os pacientes (Nome, Tempo de espera inicial, Dicionário de Sintomas)
    ana = Paciente("Ana", 2, sintomas_ana)
    bruno = Paciente("Bruno", 30, sintomas_bruno)
    carla = Paciente("Carla", 15, sintomas_carla)

    # Instanciando o problema de triagem
    lista_pacientes = [ana, bruno, carla]
    problema = Triagem(lista_pacientes)

    # Executando a busca A* utilizando a nova heurística probabilística dinâmica
    ordem_atendimento, custo_total = a_star_search(problema)

    print("\n--- RESULTADO DA TRIAGEM INTELIGENTE ---")
    print("Pacientes em fila e suas probabilidades calculadas pelo agente de IA:")
    print(lista_pacientes)

    print("\nOrdem Ótima de Atendimento (A*):", ordem_atendimento)
    print(f"Custo Total de Deterioração Minimizado: {custo_total:.2f}")