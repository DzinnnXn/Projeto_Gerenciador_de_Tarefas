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
        print("1. Criar Projeto")
        print("2. Listar Projetos")
        print("3. Adicionar Tarefa a Projeto")
        print("4. Listar Tarefas de Projeto")
        print("5. Marcar Tarefa como Concluída")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")
        match escolha:
            case 1:
                cls()
                nome_projeto = input("Digite o nome do projeto: ")
                projeto = gerenciador.criar_projeto(nome_projeto)
                print(f"Projeto '{projeto.nome}' criado com sucesso!")
                pausar()
                
            case 2:
                cls()
                print("\n----- Lista de Projetos -----")
                gerenciador.listar_projetos()
                pausar()
                
                
            case 3:
                cls()
                gerenciador.listar_projetos()
                indice_projeto = int(input("Digite o número do projeto: "))
                if 0 < indice_projeto <= len(gerenciador.projetos):
                    projeto = gerenciador.projetos[indice_projeto - 1]
                    titulo = input("Digite o título da tarefa: ")
                    descricao = input("Digite a descrição da tarefa: ")
                    prioridade = input("Digite a prioridade (Alta/Média/Baixa): ")
                    tarefa = Tarefa(titulo, descricao, prioridade)
                    projeto.adicionar_tarefa(tarefa)
                    print(f"Tarefa adicionada ao projeto '{projeto.nome}' com sucesso!")
                    pausar()   
                
            case 4:
                cls()
                gerenciador.listar_projetos()
                indice_projeto = int(input("Digite o número do projeto: "))
                if 0 < indice_projeto <= len(gerenciador.projetos):
                    projeto = gerenciador.projetos[indice_projeto - 1]
                    print(f"\n----- Lista de Tarefas do Projeto '{projeto.nome}' -----")
                    gerenciador.listar_tarefas_por_projeto(projeto)
                    pausar()
                
            case 5:
                cls()
                gerenciador.listar_projetos()
                indice_projeto = int(input("Digite o número do projeto: "))
                if 0 < indice_projeto <= len(gerenciador.projetos):
                    projeto = gerenciador.projetos[indice_projeto - 1]
                    gerenciador.listar_tarefas_por_projeto(projeto)
                    indice_tarefa = int(input("Digite o número da tarefa a marcar como concluída: "))
                    gerenciador.marcar_como_concluida(projeto, indice_tarefa)
                    pausar()
                    
            case 6:
                print("Saindo...")
                pausar()
                break
            
            case _:
                print("Opção Inválida. Tente Novamente")