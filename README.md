# 📝 Task Tracker CLI

A simple command-line tool to manage your daily tasks.  
Built as part of the [Task Tracker Project](https://roadmap.sh/projects/task-tracker).

---

## 🚀 Features
- Add, update, and delete tasks  
- Mark tasks as **todo**, **in-progress**, or **done**  
- List all or filter by status  
- Stores data in `tasks.json` with timestamps  
- Uses only Python’s built-in modules  

---

## ⚙️ Setup

### Linux / macOS
```bash
chmod +x task-cli.py
sudo mv task-cli.py /usr/local/bin/task-cli

Windows

Create a task-cli.bat file with:

python "%~dp0task-cli.py" %*

Add its folder to your PATH.
🧩 Usage

task-cli add "Buy groceries"
task-cli update 1 "Buy groceries and cook dinner"
task-cli mark-in-progress 1
task-cli mark-done 1
task-cli delete 1
task-cli list [status]

🗂 Example tasks.json

[
  {
    "id": 1,
    "description": "Buy groceries",
    "status": "done",
    "createdAt": "2025-10-14 18:39:40",
    "updatedAt": "2025-10-14 19:02:11"
  }
]

Built to practice file handling, JSON, and CLI design in Python.
Learn more at roadmap.sh/projects/task-tracker