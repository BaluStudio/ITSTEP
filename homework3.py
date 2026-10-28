# Тут завдання 1
doing=True
class Task:
    def __init__(self, name, description, deadline, progress=False):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.progress = progress

    def finish(self):
        self.deadline = None
        self.progress = True

class TaskManager:
    def __init__(self, tasks):
        self.tasks = []

    def addTask(self, task):
        self.tasks.append(task)

    def removeTask(self, task):
        self.tasks.remove(task)

    def progressOfTask(self, task):
        task.finish()

    def showTasks(self):
        for task in self.tasks:
            print(
                f"Назва завдання: {task.name} - Опис: {task.description} - Дедлайн: {task.deadline} - Статус: {task.progress}")
manager = TaskManager([])

while doing:
    print("Будь ласка, оберіть дію")
    print("(1) Показати усі завдання")
    print("(2) Додати завдання")
    print("(3) Видалити завдання")
    print("(4) Позначити завдання як виконано")
    print("(5) Вихід :(")
    option = int(input("Обирайте!"))
    if option==1:
        manager.showTasks()
    if option==2:
        name=input("Напишіть назву свого завдання, будь ласка")
        description=input("Напишіть тепер, будь ласка, опис цього завдання")
        deadline=input("Напишіть дедлайн, будь ласка, свого завдання")
        progress=False
        newTask = Task(name, description, deadline, progress)
        manager.addTask(newTask)
        print("Молодці, Ви додали нове завдання, дякую!")
    if option==3:
        found=False
        removingTask=input("Будь ласка, введіть назву завдання, яке Ви, на жаль, чи то на щастя, хочете видалити")
        for task in manager.tasks:
            if task.name==removingTask:
                manager.removeTask(task)
                found=True
                print("Молодці, або не зовсім, але Ви видалили своє завдання! Дякую!")
        if found==False:
            print("Такого завдання немає... або ви його уже видалили, або ще не додали. А також перевірте чи правильно написали!")
    if option==4:
        found=False
        finishingTask=input("Введіть, будь ласка, назву завдання, яке ви нарешті виконали")
        for task in manager.tasks:
            if task.name==finishingTask:
                found=True
                if task.progress==True:
                    print("Ви уже, на щастя, те завдання виконали, молодці!")
                else:
                    manager.progressOfTask(task)
                    print("Молодці, виконали, на щастя, своє завдання! Вітаю!")
        if found==False:
            print("Такого завдання немає... або ви його видалили, або ще не додали. А також перевірте чи правильно написали!")
    if option==5:
        doing = False
        print("Допобачення! :) Гарного вечора чи дня, а може й ранку, але усього гарного!")
