from datetime import datetime
import json
import sys



tasks = []


def add_task():
    tasks = load_tasks()
    id = generate_ID()
    title = input("Enter a title for your task: ")
    description = input("Enter a description for your task: ")
    status = "todo"
    createdAt = now()
    updatedAt = now()
    new_task = {"id": id, "title": title, "description": description, "status": status, "createdAt": createdAt, "updatedAt": updatedAt}
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"✅ Task Added Successfully (ID: {id}).")


def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def generate_ID():
    return tasks.__len__() + 1



def show_task_list():
    tasks = load_tasks()
    if tasks:
        for idx,task in enumerate(tasks, start=1):
            print(idx, task["title"])
        
    else:
        print("📭 No Tasks Available.")



def update_task():
    show_task_list()
    if tasks:
        task_index = int(input('Enter the Index of your task to be updated: '))
        if 0 <= task_index < tasks.__len__():
            new_task_title = input('Enter your new title or (Press Enter to keep current title): ')
            new_task_description = input('Enter your new description or (Press Enter to keep current description): ')
            if new_task_title == "" :
                pass
            else: 
                tasks[task_index]['title'] = new_task_title
            
            if new_task_description == "" :
                pass
            else: 
                tasks[task_index]['description'] == new_task_description

            print("✅ Task Updated")
        else:
            print("⚠️ Invalid Index.")
    else:
        print("📭 No Tasks Available.")



def delete_task():
    show_task_list()
    if tasks:
        task_index = int(input('Enter the Index of the task to be deleted: '))
        if 0 <= task_index < tasks.__len__():
            deleted_task = tasks.pop(task_index)
            print(f"🗑️ Task '{deleted_task['title']}' deleted successfully.")
        else: 
            print("⚠️ Invalid Index.")
    else:
        print("📭 No Tasks Available.")


def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            tasks.append(json.load(f))
    
    except FileNotFoundError:
        return []

def save_tasks():
    with open('tasks.json', 'w') as f:
        json.dump(tasks[0], f, indent=4)


# load_tasks()
print(tasks)