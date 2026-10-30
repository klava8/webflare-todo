"""Простой консольный список задач."""
from tasks import add_task, complete_task


def main():
    """Выполнять команды до выхода пользователя."""
    tasks = []
    while True:
        command = input("add / list / done / exit: ").strip()
        try:
            if command == "exit":
                break
            if command == "add":
                print("Добавлена:", add_task(tasks, input("Название: ")))
            elif command == "list":
                for task in tasks:
                    mark = "x" if task["done"] else " "
                    print(f"{task['id']}. [{mark}] {task['title']}")
            elif command == "done":
                complete_task(tasks, int(input("Номер: ")))
                print("Готово")
            else:
                print("Неизвестная команда")
        except ValueError as error:
            print("Ошибка:", error)


if __name__ == "__main__":
    try:
        main()
    except EOFError:
        print("Ввод завершён")
