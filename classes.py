class Tarefa:
    def __init__(self, titulo, descricao, data_vencimento, prioridade):
        self.titulo = titulo
        self.descricao = descricao
        self.data_vencimento = data_vencimento
        self.prioridade = prioridade
        self.concluida = False

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def listar_tarefas(self):
        for i, tarefa in enumerate(self.tarefas, start=1):
            status = "Concluída" if tarefa.concluida else "Pendente"
            print(f"{i}. {tarefa.titulo} ({status})")

    def marcar_como_concluida(self, indice):
        if 0 < indice <= len(self.tarefas):
            self.tarefas[indice - 1].concluida = True