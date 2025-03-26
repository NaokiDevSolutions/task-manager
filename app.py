import json 
import os

TASK_FILE = "task.json"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    tasks = load_tasks()
    task = {"id": len(tasks) +1, "description": description, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    return f"Tarefa '{description}' adicionada!"

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        return "Nenhuma tarefa disponível."
    
    return "\n".join([f"[{'✔' if task['completed'] else '✖'}] {task['id']}: {task["description"]}" for task in tasks])

def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            return f"tarefa '{task['description']}' marcada como concluída!"
    return "Tarefa não encontrada."

def remove_task(taks_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != taks_id]
    save_tasks(tasks)
    return f"Tarefa {taks_id} removida com sucesso!"

if __name__ == "__main__":
    print(add_task("Estudar Github"))
    print(add_task("Criar repositório"))
    print(list_tasks())
    print(complete_task(1))
    print(remove_task(2))
    print(list_tasks())
