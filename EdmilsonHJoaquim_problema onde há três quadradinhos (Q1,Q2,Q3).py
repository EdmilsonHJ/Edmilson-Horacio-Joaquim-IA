#Mini-Teste1 - Edmilson Horacio Joaquim
import random

class Ambiente:
    def __init__(self):
        self.estado = {Q1: random.choice(['cheio', 'vazio']),
                       Q2: random.choice(['cheio', 'vazio']),
                       Q3: random.choice(['cheio', 'vazio'])}
        self.accao = ['encher', 'esquerda', 'direita']

    def percepcao(self, agente):
        return (agente.localizacao, self.estado[agente.localizacao])

    def localizacao_default(self):
        return random.choice([Q1, Q2, Q3])

    def executar_accao(self, accao, agente):
        if accao == 'esquerda':
            agente.performace -= 1
        elif accao == 'direita':
            agente.performace -= 1
        elif accao == 'encher':
            agente.performace += 10
            self.estado[agente.localizacao] = "cheio"

class Agente:
    def __init__(self, localizacao):
        self.performace = 0
        self.localizacao = localizacao

    def programa_tabela(self, percepcao):
        modelo = {Q1: None, Q2: None, Q3: None}
        localizacao, estado = percepcao

        tabela = {(Q1, 'cheio'): 'direita',
                  (Q1, 'vazio'): 'encher',
                  (Q2, 'cheio'): 'esquerda',
                  (Q2, 'vazio'): 'encher',
                  (Q3, 'cheio'): 'esquerda',
                  (Q3, 'vazio'): 'encher',
                  ((Q1, 'vazio'), (Q1, 'cheio')): 'esquerda',
                  ((Q1, 'cheio'), (Q2, 'vazio')): 'encher',
                  ((Q2, 'cheio'), (Q1, 'vazio')): 'encher',
                  ((Q2, 'vazio'), (Q2, 'cheio')): 'encher',
                  ((Q1, 'vazio'), (Q1, 'cheio'), (Q2, 'vazio')): 'encher',
                  ((Q2, 'vazio'), (Q2, 'cheio'), (Q1, 'vazio')): 'encher',
                  ((Q2, 'vazio'), (Q2, 'cheio'), (Q3, 'vazio')): 'encher',
                  ((Q3, 'vazio'), (Q3, 'cheio'), (Q2, 'vazio')): 'encher'}

        return tabela.get(percepcao)

# Main
percepcoes = []
Q1, Q2, Q3 = (0,0), (0,1), (0,2)

ambiente = Ambiente()
print("Estado do Ambiente:", ambiente.estado)
localizacao_agente = ambiente.localizacao_default()
agente = Agente(localizacao_agente)
percepcao = ambiente.percepcao(agente)
accao = agente.programa_tabela(percepcao)
ambiente.executar_accao(accao, agente)

print("Percepção:", percepcao)
print("Ação a Realizar:", accao)
print("Pontuação:", agente.performace)
print("Estado do Ambiente:", ambiente.estado)

# Trocar de Localizacao
localizacao_agente = Q1 if agente.localizacao == Q2 else Q2 if agente.localizacao == Q3 else Q3
agente.localizacao = localizacao_agente
percepcao = ambiente.percepcao(agente)
accao = agente.programa_tabela(percepcao)
ambiente.executar_accao(accao, agente)

print("\nDepois de mudar de localização:")
print("Localização do Agente:", agente.localizacao)
print(percepcao)
