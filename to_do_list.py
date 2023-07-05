print("###!!! LISTA DE TAREFAS !!!###")

tasks = []
user_list = input("DIGITE A SUA LISTA DE TAREFAS: ")

while user_list:
    tasks.append(user_list)
    user_list = input("DIGITE A SUA LISTA DE TAREFAS (ou pressione enter para finalizar): ")
    print(tasks)

print (" DIGITE 0 PARA MARCAR A PRIMEIRA COMO CONCLUIDA\n", "DIGITE 1 PARA MARCAR A SEGUNDA COMO CONCLUIDA\n", "DIGITE 2 PARA MARCAR A TERCEIRA COMO CONCLUIDA\n", "E ASSIM POR DIANTE")

while True:
    complete = input("Digite o número da tarefa que foi concluída (ou pressione enter para finalizar): ")
    if not complete:
        break
    elif not complete.isdigit() or int(complete) >= len(tasks):
        print("Número de tarefa inválido.")
    else:
        tasks[int(complete)] += "(Completa)"
        print("\n".join(tasks))
print ("Tarefas concluidas")


