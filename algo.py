from classes import *
import os

def pausar():
    os.system("pause")
    
def cls():
    os.system("cls")

gerenciador = GerenciadorTarefas()

def main():
    s = 0
    while s == 0:
        cls()
        print("\n----- Gerenciador de Tarefas -----")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar como Concluída")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cls()
            titulo = input("Digite o título da tarefa: ")
            descricao = input("Digite a descrição da tarefa: ")
            data_vencimento = input("Digite a data de vencimento (dd/mm/aaaa): ")
            prioridade = input("Digite a prioridade (Alta/Média/Baixa): ")
            tarefa = Tarefa(titulo, descricao, data_vencimento, prioridade)
            gerenciador.adicionar_tarefa(tarefa)
            print("Tarefa adicionada com sucesso!")
            pausar()

        elif escolha == "2":
            cls()
            print("\n----- Lista de Tarefas -----")
            gerenciador.listar_tarefas()
            pausar()

        elif escolha == "3":
            cls()
            gerenciador.listar_tarefas()
            indice = int(input("Digite o número da tarefa a marcar como concluída: "))
            gerenciador.marcar_como_concluida(indice)
            print("Tarefa marcada como concluída!")
            pausar()

        elif escolha == "4":
            cls()
            print("Saindo...")
            pausar()
            break

        else:
            print("Opção inválida. Tente novamente.")