import random
import os

#Função para listar tarefas
def listaTarefa(tarefas):
    for id, tarefa in enumerate(tarefas, start = 1):
        print(f"{id}. {tarefa}")

#Função para registrar uma nova tarefa
def registraTarefa(tarefas, descricao):
    novaTarefa = f"{len(tarefas)+1}.{descricao.capitalize()} []"
    tarefas.append(novaTarefa)
    print("Tarefa Registrada!!!")

#Função para marcar tarefa como realizada
def tarefaRealizada(tarefas, identificador):
    if identificador <= tarefas <= len(tarefas):
        tarefaa = tarefas.pop(identificador)
        tarefa = tarefa[:-3] + "[x]"
        tarefas.insert(0, tarefa)
        print("Tarefa Realizada!!!")
    
    else:
        print("Identificador Inválido!!")

#Função para editar tarefa
def editarTarefa(tarefas, identificador, novaDescricao):
    if 1 <= identificador <= len(tarefas):
        tarefa = tarefas [identificador -1]
        statusBox = tarefa[-3:]
        novaTarefa = f"{identificador}.{novaDescricao} {statusBox}"
        tarefas[identificador - 1] = novaTarefa
        print("Tarefa Editada!!!")

    else:
        print("Identificador Inválido!")



#Função para salvar uma tarefa em um arquivo
def salvarTarefas(tarefas, nomeArquivo = "tarefas.txt"):
    with open(nomeArquivo, "w") as arquivo:
        for tarefa in tarefas:
            arquivo.write(tarefa + "\n")


#função para carregar tarefas de um arquivo
def carregarTarefas(nomeArquivo = "tarefas.txt"):
    tarefas = []
    if os.path.exists(nomeArquivo):
        with open(nomeArquivo, "r") as arquivo:
            tarefas = [linha.strip() for linha in arquivo]
    
    return tarefas
        

arquivoTarefas = "tarefas.txt"
tarefas = carregarTarefas(arquivoTarefas)

while True:
    print("\n ========== Gerenciador de Tarefas ==========")
    print("1- Listar Tarefas")
    print("2- Registrar Nova Tarefa")
    print("3- Marcar Tarefa Como Registrada")
    print("4- Editar Tarefa")
    print("5- Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        listaTarefa(tarefas)
    elif opcao == "2":
        descricao = input("Indique a descricao da nova tarefa: ")
        registraTarefa = (tarefas, descricao)
    elif opcao == "3":
        identificador = int(input("Tarefa a ser marcada como realizada: "))
    elif opcao == "4":
        identificador = int(input("Tarefa a ser editada: "))
        novaDescricao = input("Digite a nova descricao da tarefa: ")
        editarTarefa = (tarefas, identificador, novaDescricao)
    elif opcao == "5":
        salvarTarefas(tarefas, arquivoTarefas)
        print("Tarefas salvas. Saindo...")
        break
    else: 
        ("Opcao inválida, tente novamente!")



