from datetime import datetime
import json
import sys


tasks = []


def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
           data = json.load(f)
        
        if isinstance(data, dict):
            return [data]
        return data
    
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)


def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# def generate_ID():
#     return tasks[-1]["id"] + 1 if tasks else 1 


def add_task(description):
    tasks = load_tasks()
    id = tasks[-1]["id"] + 1 if tasks else 1
    new_task = {"id": id, 
                "description": description, 
                "status": "todo", 
                "createdAt": now(), 
                "updatedAt": now()}
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"✅ Task Added Successfully (ID: {id}).")



def show_tasks_list(task_filter=None):
    tasks = load_tasks()
    if task_filter not in ["todo", "in-progress", "done", None]:
        print("⚠️ Invalid status.")    
        return   

    if task_filter:
        tasks = [t for t in tasks if t["status"] == task_filter]

    if tasks:
        for t in tasks:
            print(f"[{t['id']}] {t['description']} ({t['status']})")
            print(f"   Created: {t['createdAt']}  |  Updated: {t['updatedAt']}")
            # print(f"ID: {t["id"]}, Description: {t["description"]}, status: {t["status"]}\n")

    if not tasks:
        print("📭 No Tasks Available.")
        return



def update_task(task_id, new_description):
    tasks = load_tasks()
    if tasks:
        for t in tasks:
            if t["id"] == task_id:
                t["description"] = new_description
                t["updatedAt"] = now()
                save_tasks(tasks)
                print("✅ Task Updated")
                return
        print("⚠️ Invalid ID.")
    else:
        print("📭 No Tasks Available.")



def delete_task(task_id):
    tasks = load_tasks()
    if tasks:
        new_tasks = [t for t in tasks if t["id"] != task_id]
        if len(new_tasks) == len(tasks):
            print("⚠️ Invalid Index.")

        else:
            save_tasks(new_tasks)
            print(f"🗑️ Task {task_id} deleted successfully")
    
    else:
        print("📭 No Tasks Available.")


def mark_status(task_id, new_status):
    tasks = load_tasks()
    if tasks:
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = new_status
                task["updatedAt"] = now()
                save_tasks(tasks)
                print(f"Task {task_id} marked as {new_status}")
                return
        print("⚠️ Invalid Index.")

    else:
        print("📭 No Tasks Available.")


def delete_all():
    tasks = load_tasks()
    for t in tasks:
        delete_task(t["id"])


def main():
    args = sys.argv[1:]

    if not args:
        print("\nUsage:")
        print("  add \"task description\"")
        print("  update <id> \"new description\"")
        print("  delete <id>")
        print("  mark-in-progress <id>")
        print("  mark-done <id>")
        print("  list [status]\n")
        return
    
    cmd = args[0]

    if cmd == "add":
        description = " ".join(args[1:])
        if not description:
            print("Error: description required")
            return
        add_task(description)

    elif cmd == "update":
        update_task(int(args[1]), " ".join(args[2:]))

    elif cmd == "delete":
        delete_task(int(args[1]))

    elif cmd == "delete-all":
        delete_all()

    elif cmd == "mark-in-progress":
        mark_status(int(args[1], "in-progress")) 

    elif cmd == "mark-done":
        mark_status(int(args[1]), "done")

    elif cmd == "list":
        show_tasks_list(args[1] if len(args) > 1 else None)

    else:
        print("Unknown command")

        
if __name__ == "__main__" :
    main()
