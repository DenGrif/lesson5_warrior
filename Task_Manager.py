class Task:
    def __init__(self, description, deadline):
        """
        Инициализация задачи с описанием и сроком выполнения.
        По умолчанию задача не выполнена.
        """
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        """
        Отметить задачу как выполненную.
        """
        self.completed = True

    def __repr__(self):
        """
        Вернуть строковое представление задачи.
        """
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"

class TaskManager:
    def __init__(self):
        """
        Инициализация менеджера задач.
        """
        self.tasks = []

    def add_task(self, description, deadline):
        """
        Добавить новую задачу в список.
        """
        task = Task(description, deadline)
        self.tasks.append(task)

    def mark_task_completed(self, index):
        """
        Отметить задачу как выполненную по её индексу в списке.
        """
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
        else:
            print("Задача с таким индексом не существует.")

    def get_pending_tasks(self):
        """
        Вернуть список всех невыполненных задач.
        """
        return [task for task in self.tasks if not task.completed]

    def show_tasks(self):
        """
        Показать все задачи с их статусами.
        """
        if not self.tasks:
            print("Задач нет.")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

# Пример использования
manager = TaskManager()
manager.add_task("Закончить проект", "2024-09-30")
manager.add_task("Купить продукты", "2024-09-25")
manager.show_tasks()

manager.mark_task_completed(0)
print("\nТекущие задачи:")
for task in manager.get_pending_tasks():
    print(task)
