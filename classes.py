class Tarefa:
    def __init__(self, titulo, descricao, prioridade):
        self.titulo = titulo
        self.descricao = descricao
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
            print(f"{i}. {tarefa.titulo} ({tarefa.prioridade}) - {status}")

    def marcar_como_concluida(self, indice):
        match indice:
            case 0:
                print("Índice inválido. Tente novamente.")
            case _ if 0 < indice <= len(self.tarefas):
                tarefa = self.tarefas[indice - 1]
                tarefa.concluida = True
                self.tarefas.pop(indice - 1)  # Remove a tarefa da lista
            case _:
                print("Índice inválido. Tente novamente.")