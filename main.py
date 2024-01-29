import csv

def load_tasks():
    try:
        with open('tasks.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            return [list(map(str, row)) for row in reader]
    except FileNotFoundError:
        return []

def save_tasks(list_tache):
    with open('tasks.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(list_tache)

def add(list_tache):
    print("Saisir la tâche : ")
    tache = input()
    list_tache.append([tache, 1])
    save_tasks(list_tache)
    app(list_tache)

def delete(list_tache):
    print("Saisir le numéro de la tâche à supprimer : ")
    sup = input()
    del(list_tache[int(sup)-1])
    save_tasks(list_tache)
    app(list_tache)

def do(list_tache):
    print("Saisir le numéro de la tâche finie : ")
    fin = input()
    list_tache[int(fin)-1][1] = 0
    save_tasks(list_tache)
    app(list_tache)

def app(list_tache):
    print("To Do List :")
    print("___________")
    for i in range(len(list_tache)):
        if list_tache[i][1] == 0:
            print(f"{i+1} : {list_tache[i][0]} ==> FINI")
        else:
            print(f"{i+1} : {list_tache[i][0]} ==> A FAIRE")

    print("___________")
    print("Add : 0")
    print("Delete : 1")
    print("Do : 2")
    print("Close : 3")
    test = input()
    if test == "0":
        return add(list_tache)
    elif test == "1":
        return delete(list_tache)
    elif test == "2":
        return do(list_tache)
    else:
        return "Fin"

if __name__ == '__main__':
    tasks = load_tasks()
    app(tasks)
