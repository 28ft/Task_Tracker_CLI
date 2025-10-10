from datetime import datetime




tasks_list = ["jshad","uhwk","ihuw"]

def create_task():
    id = generate_ID()
    title = input("Enter a title for your task: ")
    description = input("Enter a description for your task: ")
    createdAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tasks_list.append({"id": id, "title": title, "description": description, "createdAt": createdAt, "updatedAt": updatedAt})
    print("✅ Task Created Successfully.")


def generate_ID():
    return tasks_list.__len__() + 1

def show_task_list():
    if tasks_list:
        for idx,task in enumerate(tasks_list, start=1):
            print(idx, task['title'])
        
    else:
        print("📭 No Tasks Available.")


# show_task_list()
# create_task()
# show_task_list()
# print(tasks_list)

