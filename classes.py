class Tarefa:
    def __init__(self, titulo, descricao, prioridade):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.concluida = False

class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
        tarefa.projeto_associado = self

class GerenciadorTarefas:
    def __init__(self):
        self.projetos = []

    def criar_projeto(self, nome):
        projeto = Projeto(nome)
        self.projetos.append(projeto)
        return projeto

    def listar_projetos(self):
        for i, projeto in enumerate(self.projetos, start=1):
            print(f"{i}. {projeto.nome}")

    def listar_tarefas_por_projeto(self, projeto):
        for i, tarefa in enumerate(projeto.tarefas, start=1):
            status = "Concluída" if tarefa.concluida else "Pendente"
            print(f"{i}. {tarefa.titulo} ({tarefa.prioridade}) - {status}")

    def marcar_como_concluida(self, projeto, indice):
        if 0 < indice <= len(projeto.tarefas):
            projeto.tarefas[indice - 1].concluida = True