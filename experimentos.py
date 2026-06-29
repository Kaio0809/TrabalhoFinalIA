from IA.TrabalhoFinal.TrabalhoFinalIA.busca import Paciente, a_star_search, Triagem

def fifo(lista: list[Paciente]):
    return sorted(lista, key=lambda paciente: paciente.tempo_inicial_fila, reverse=True)

def gulosa(lista: list[Paciente]):
    return  sorted(lista, key=lambda paciente: paciente.prob_gravidade_alta, reverse=True)

def comparar(lista:list[Paciente]):
    print('\nFIFO: ')
    for p in fifo(lista):
        print(f' - {p.nome}: {p.tempo_inicial_fila}m', end="")
    print('\n\nGulosa: ')
    for p in gulosa(lista):
        print(f' - {p.nome}: {p.prob_gravidade_alta:.3f}', end="")
    print('\n\nA*: ')
    problema = Triagem(lista)
    ordem_atendimento, custo_total = a_star_search(problema)
    for p in ordem_atendimento:
        print(f' - {p.nome}: (P {p.prob_gravidade_alta:.3f}), (Tempo {p.tempo_inicial_fila}m)')
    print('Custo Total de Deteriorização: ', custo_total)

# Testes

sintomas_daniel = {
    'Febre': 'Sim',
    'Saturacao_O2': 'Critica',
    'Pressao_Arterial': 'Baixa',
    'Idade': 'Adulto',
    'Doenca_Cronica': 'Sim'
}

sintomas_elisa = {
    'Febre': 'Nao',
    'Saturacao_O2': 'Normal',
    'Pressao_Arterial': 'Normal',
    'Idade': 'Crianca',
    'Doenca_Cronica': 'Nao'
}

sintomas_felipe = {
    'Febre': 'Sim',
    'Saturacao_O2': 'Reduzida',
    'Pressao_Arterial': 'Normal',
    'Idade': 'Idoso',
    'Doenca_Cronica': 'Sim'
}

sintomas_gabriela = {
    'Febre': 'Nao',
    'Saturacao_O2': 'Reduzida',
    'Pressao_Arterial': 'Baixa',
    'Idade': 'Adulto',
    'Doenca_Cronica': 'Nao'
}

sintomas_henrique = {
    'Febre': 'Sim',
    'Saturacao_O2': 'Normal',
    'Pressao_Arterial': 'Normal',
    'Idade': 'Adulto',
    'Doenca_Cronica': 'Nao'
}

daniel = Paciente("Daniel", 5, sintomas_daniel)
elisa = Paciente("Elisa", 10, sintomas_elisa)
felipe = Paciente("Felipe", 15, sintomas_felipe)
gabriela = Paciente("Gabriela", 20, sintomas_gabriela)
henrique = Paciente("Henrique", 25, sintomas_henrique)

lista_de_pacientes = [daniel, elisa, felipe, gabriela, henrique]
print('Cenário 1: 5 Pacientes')
comparar(lista_de_pacientes)

sintomas_igor = {
    'Febre': 'Sim',
    'Saturacao_O2': 'Critica',
    'Pressao_Arterial': 'Baixa',
    'Idade': 'Idoso',
    'Doenca_Cronica': 'Sim'
}

sintomas_julia = {
    'Febre': 'Nao',
    'Saturacao_O2': 'Normal',
    'Pressao_Arterial': 'Normal',
    'Idade': 'Adulto',
    'Doenca_Cronica': 'Nao'
}

sintomas_karla = {
    'Febre': 'Sim',
    'Saturacao_O2': 'Reduzida',
    'Pressao_Arterial': 'Normal',
    'Idade': 'Crianca',
    'Doenca_Cronica': 'Nao'
}

sintomas_lucas = {
    'Febre': 'Sim',
    'Saturacao_O2': 'Critica',
    'Pressao_Arterial': 'Baixa',
    'Idade': 'Adulto',
    'Doenca_Cronica': 'Nao'
}

sintomas_mariana = {
    'Febre': 'Nao',
    'Saturacao_O2': 'Reduzida',
    'Pressao_Arterial': 'Normal',
    'Idade': 'Idoso',
    'Doenca_Cronica': 'Sim'
}

sintomas_nicolas = {
    'Febre': 'Nao',
    'Saturacao_O2': 'Normal',
    'Pressao_Arterial': 'Baixa',
    'Idade': 'Adulto',
    'Doenca_Cronica': 'Nao'
}

sintomas_olivia = {
    'Febre': 'Sim',
    'Saturacao_O2': 'Reduzida',
    'Pressao_Arterial': 'Baixa',
    'Idade': 'Idoso',
    'Doenca_Cronica': 'Sim'
}

sintomas_pedro = {
    'Febre': 'Nao',
    'Saturacao_O2': 'Normal',
    'Pressao_Arterial': 'Normal',
    'Idade': 'Crianca',
    'Doenca_Cronica': 'Nao'
}

sintomas_quezia = {
    'Febre': 'Sim',
    'Saturacao_O2': 'Critica',
    'Pressao_Arterial': 'Normal',
    'Idade': 'Adulto',
    'Doenca_Cronica': 'Sim'
}

sintomas_rafael = {
    'Febre': 'Sim',
    'Saturacao_O2': 'Normal',
    'Pressao_Arterial': 'Normal',
    'Idade': 'Adulto',
    'Doenca_Cronica': 'Nao'
}

sintomas_sara = {
    'Febre': 'Nao',
    'Saturacao_O2': 'Reduzida',
    'Pressao_Arterial': 'Baixa',
    'Idade': 'Adulto',
    'Doenca_Cronica': 'Sim'
}

sintomas_tiago = {
    'Febre': 'Sim',
    'Saturacao_O2': 'Critica',
    'Pressao_Arterial': 'Baixa',
    'Idade': 'Idoso',
    'Doenca_Cronica': 'Nao'
}

sintomas_ursula = {
    'Febre': 'Nao',
    'Saturacao_O2': 'Normal',
    'Pressao_Arterial': 'Normal',
    'Idade': 'Idoso',
    'Doenca_Cronica': 'Sim'
}

sintomas_victor = {
    'Febre': 'Sim',
    'Saturacao_O2': 'Reduzida',
    'Pressao_Arterial': 'Normal',
    'Idade': 'Adulto',
    'Doenca_Cronica': 'Sim'
}

sintomas_wagner = {
    'Febre': 'Nao',
    'Saturacao_O2': 'Critica',
    'Pressao_Arterial': 'Baixa',
    'Idade': 'Adulto',
    'Doenca_Cronica': 'Nao'
}

sintomas_ximena = {
    'Febre': 'Sim',
    'Saturacao_O2': 'Normal',
    'Pressao_Arterial': 'Baixa',
    'Idade': 'Crianca',
    'Doenca_Cronica': 'Nao'
}

sintomas_yasmin = {
    'Febre': 'Nao',
    'Saturacao_O2': 'Reduzida',
    'Pressao_Arterial': 'Normal',
    'Idade': 'Adulto',
    'Doenca_Cronica': 'Nao'
}

sintomas_zeca = {
    'Febre': 'Sim',
    'Saturacao_O2': 'Critica',
    'Pressao_Arterial': 'Baixa',
    'Idade': 'Idoso',
    'Doenca_Cronica': 'Sim'
}

sintomas_amanda = {
    'Febre': 'Nao',
    'Saturacao_O2': 'Normal',
    'Pressao_Arterial': 'Normal',
    'Idade': 'Adulto',
    'Doenca_Cronica': 'Sim'
}

sintomas_brenda = {
    'Febre': 'Sim',
    'Saturacao_O2': 'Reduzida',
    'Pressao_Arterial': 'Baixa',
    'Idade': 'Adulto',
    'Doenca_Cronica': 'Nao'
}

igor = Paciente("Igor", 5, sintomas_igor)
julia = Paciente("Julia", 10, sintomas_julia)
karla = Paciente("Karla", 15, sintomas_karla)
lucas = Paciente("Lucas", 20, sintomas_lucas)
mariana = Paciente("Mariana", 25, sintomas_mariana)
nicolas = Paciente("Nicolas", 30, sintomas_nicolas)
olivia = Paciente("Olivia", 35, sintomas_olivia)
pedro = Paciente("Pedro", 40, sintomas_pedro)
quezia = Paciente("Quezia", 45, sintomas_quezia)
rafael = Paciente("Rafael", 50, sintomas_rafael)
sara = Paciente("Sara", 55, sintomas_sara)
tiago = Paciente("Tiago", 60, sintomas_tiago)
ursula = Paciente("Ursula", 65, sintomas_ursula)
victor = Paciente("Victor", 70, sintomas_victor)
wagner = Paciente("Wagner", 75, sintomas_wagner)
ximena = Paciente("Ximena", 80, sintomas_ximena)
yasmin = Paciente("Yasmin", 85, sintomas_yasmin)
zeca = Paciente("Zeca", 90, sintomas_zeca)
amanda = Paciente("Amanda", 95, sintomas_amanda)
brenda = Paciente("Brenda", 100, sintomas_brenda)


lista_caso2 = [igor,julia,karla,lucas,mariana,nicolas,olivia,pedro,quezia,rafael,sara,tiago,ursula,victor,wagner,ximena,yasmin,zeca,amanda,brenda]
print('\nCenário 2: 20 Pacientes')
comparar(lista_caso2)
