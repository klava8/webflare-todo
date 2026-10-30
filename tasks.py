"""Хранение задач в памяти."""


def add_task(tasks, title):
    """Добавить непустую задачу и вернуть её номер."""
    title = title.strip()
    if not title:
        raise ValueError("Название не должно быть пустым")
    task = {"id": len(tasks) + 1, "title": title, "done": False}
    tasks.append(task)
    return task["id"]


def complete_task(tasks, task_id):
    """Отметить существующую задачу выполненной."""
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return
    raise ValueError("Задача не найдена")
