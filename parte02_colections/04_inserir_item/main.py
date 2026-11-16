# Bibliotecas
import os

tarefas = [] # Lista vazia

os.system("cls" if os.name == "nt" else "clear") # Limpa terminal

# Loop
while True:
    # Menu
    print("1 - Inserir nova tarefa na lista")
    print("2 - Finalizar e exibir lista")
    opcao = input("Opção desejada: ").strip() # Informa opção desejada

    # Verifica a opção informada
    match opcao:
        case "1":
            nova_tarefa = input("Informe a nova tarefa: ") # Informa novo item
            tarefas.append(nova_tarefa) # Insere item na lista
            continue # Retorna para o início do loop
        case "2":
            os.system("cls" if os.name == "nt" else "clear")

            # Exibe a lista
            for n, tarefa in enumerate(tarefas, start=1):
                print(f"{n}ª tarefa: {tarefa}")
            break # Encerra o loop
        case _:
            print("Opção inválida.")