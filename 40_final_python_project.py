# Final Python Project: Advanced Todo List Application

"""
A complete command-line Todo List application demonstrating:
- Object-Oriented Programming
- File Handling (JSON)
- Exception Handling
- Best Practices & Clean Code
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional

class TodoItem:
    """Represents a single todo item."""
    
    def __init__(self, task: str, priority: str = "medium", due_date: Optional[str] = None):
        self.task = task
        self.completed = False
        self.priority = priority.lower()
        self.created_at = datetime.now().isoformat()
        self.due_date = due_date

    def to_dict(self) -> Dict:
        return {
            "task": self.task,
            "completed": self.completed,
            "priority": self.priority,
            "created_at": self.created_at,
            "due_date": self.due_date
        }

    @classmethod
    def from_dict(cls, data: Dict):
        todo = cls(data["task"], data.get("priority", "medium"), data.get("due_date"))
        todo.completed = data.get("completed", False)
        todo.created_at = data.get("created_at", datetime.now().isoformat())
        return todo

    def __str__(self):
        status = "✓" if self.completed else " "
        due = f" (due: {self.due_date})" if self.due_date else ""
        return f"[{status}] {self.task}{due} [{self.priority}]"


class TodoList:
    """Main Todo List Manager."""
    
    def __init__(self, filename: str = "todos.json"):
        self.filename = filename
        self.todos: List[TodoItem] = self._load_todos()

    def _load_todos(self) -> List[TodoItem]:
        """Load todos from JSON file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return [TodoItem.from_dict(item) for item in data]
            except Exception:
                print("Error loading file. Starting fresh.")
        return []

    def _save_todos(self):
        """Save todos to JSON file."""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([todo.to_dict() for todo in self.todos], f, indent=2)

    def add(self, task: str, priority: str = "medium", due_date: Optional[str] = None):
        """Add a new todo item."""
        todo = TodoItem(task, priority, due_date)
        self.todos.append(todo)
        self._save_todos()
        print(f"✅ Added: {task}")

    def list_todos(self, show_completed: bool = True):
        """Display all todos."""
        if not self.todos:
            print("No tasks yet!")
            return

        print("\n=== Your Todo List ===")
        for i, todo in enumerate(self.todos, 1):
            if show_completed or not todo.completed:
                print(f"{i:2}. {todo}")

    def complete(self, index: int):
        """Mark a task as completed."""
        if 1 <= index <= len(self.todos):
            self.todos[index-1].completed = True
            self._save_todos()
            print(f"✅ Completed: {self.todos[index-1].task}")
        else:
            print("Invalid task number!")

    def delete(self, index: int):
        """Delete a task."""
        if 1 <= index <= len(self.todos):
            deleted = self.todos.pop(index-1)
            self._save_todos()
            print(f"🗑️  Deleted: {deleted.task}")
        else:
            print("Invalid task number!")

    def clear_completed(self):
        """Remove all completed tasks."""
        before = len(self.todos)
        self.todos = [todo for todo in self.todos if not todo.completed]
        self._save_todos()
        print(f"Cleared {before - len(self.todos)} completed tasks.")


# Main Application
if __name__ == "__main__":
    todo_app = TodoList()

    print("🚀 Welcome to Advanced Todo List!")
    print("=" * 40)

    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Clear completed")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            task = input("Enter task: ")
            priority = input("Priority (low/medium/high): ") or "medium"
            due = input("Due date (YYYY-MM-DD, optional): ") or None
            todo_app.add(task, priority, due)

        elif choice == "2":
            todo_app.list_todos()

        elif choice == "3":
            todo_app.list_todos(show_completed=False)
            try:
                idx = int(input("Enter task number to complete: "))
                todo_app.complete(idx)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            todo_app.list_todos()
            try:
                idx = int(input("Enter task number to delete: "))
                todo_app.delete(idx)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            todo_app.clear_completed()

        elif choice == "6":
            print("👋 Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")