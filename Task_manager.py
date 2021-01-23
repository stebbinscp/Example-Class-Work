from datetime import datetime
import sys
import pickle
import random
import re

class Task():
    """Attributes:
    - created - date
    - completed - date
    - name - string
    - unique id - number
    - priority - string value of 1, 2, or 3 default of 1
    - due date - date, optional"""

    from datetime import datetime  

    def __init__(self, name=None, due=None, priority =1):
        self.name = name
        self.due = due
        self.priority = priority
        self.created = datetime.now() 
        self.daymade = self.created.day
        self.completed = "--"

        self.age = 0

        id_list = list("abcdefghijklmnopqrstuvwxyz1234567890")

        self.unique_id = "".join(random.sample(id_list, 6))

class Tasks():
    """A list of tasks including methods
    - add (keyword add followed by the name, optional due date, and optional priority)
    - delete (keyword delete followed by the unique id to permanently delete it)
    - report (list all tasks, both completed and uncompleted)
    - list (list out all uncompleted tasks)
    - done (type keyword done and the unique id of the task to mark it as complete)"""

    def unpickle(self):
        """Unpickle the .todo.pickle file to gain access to stored task objects"""
        try:
            with open(".todo.pickle", "rb") as f:
                tasks = pickle.load(f)
            # print(type(tasks))
            # return tasks
        except:
            tasks = [] 
            # return tasks
        return tasks
  

    def add(self, task_obj):
        """Adds a new task"""
        t_asks = Tasks()
        pickled_list = t_asks.unpickle()
        pickled_list.append(task_obj)
        with open(".todo.pickle", "wb") as f:
            pickle.dump(pickled_list,f)
        # print(pickled_list)

    def remove(self, id):
        """Removes the task with the given id"""
        t_asks = Tasks()
        pickled_list = t_asks.unpickle()
        for i in pickled_list:
            if i.unique_id == id:
                pickled_list.remove(i)
        with open(".todo.pickle", "wb") as f:
            pickle.dump(pickled_list,f)

    def report(self):
        """Print out all tasks"""
        print("ID   AGE   DUE DATE      PRIORITY      TASK     Created     Completed")
        print("--   ---   --------      --------      ----     -------     ---------")
        t_asks = Tasks()
        pickled_list = t_asks.unpickle()
        for i in pickled_list:
            i.age = datetime.now().day - i.created.day
            print(f"{i.unique_id}   {i.age}   {i.due}     {i.priority}   {i.name}    {i.created}   {i.completed}")

    def list(self, search=None):
        """Print out uncompleted items"""
        print("ID   AGE   DUE DATE      PRIORITY      TASK")
        print("--   ---   --------      --------      ----")
        t_asks = Tasks()
        to_print = []
        pickled_list = t_asks.unpickle()
        if search:
            to_look = re.findall(r'\w',search)
            # print(to_look)
            for i in pickled_list:
                if "".join(to_look) in i.name:
                    if i.completed == "--":
                        to_print.append(i)
            for i in to_print:
                i.age = datetime.now().day - i.created.day
                print(f"{i.unique_id}   {i.age}   {i.due}        {i.priority}      {i.name}")
        else:
            for i in pickled_list:
                if i.completed == "--":
                    i.age = datetime.now().day - i.created.day
                    print(f"{i.unique_id}   {i.age}   {i.due}        {i.priority}      {i.name}")
    
    def done(self, id):
        """Marks the given id task as completed and the date of completion"""
        t_asks = Tasks()
        pickled_list = t_asks.unpickle()
        for i in pickled_list:
            if i.unique_id == id:
                i.completed = datetime.now()
                i.due = "--"
        with open(".todo.pickle", "wb") as f:
            pickle.dump(pickled_list,f)


# print(t.created)
# print(t_2.add(t))

def main():
    t_2 = Tasks()
    if sys.argv[1] == "add":
        if len(sys.argv) == 3:
            t = Task(sys.argv[2])
            t_2.add(t)
        elif len(sys.argv) == 4:
            t = Task(sys.argv[2], due = sys.argv[3])
            t_2.add(t)
        elif len(sys.argv) == 5:
            t = Task(sys.argv[2], due = sys.argv[3], priority = sys.argv[4])
            t_2.add(t)
        print(f"Added Task {t.unique_id}")
    elif sys.argv[1] == "remove":
        t = Task(sys.argv[2])
        t_2.remove(t.name)
        print(f"Removed Task {t.unique_id}")
    elif sys.argv[1] == "done":
        t = Task(sys.argv[2])
        t_2.done(t.name)
        print(f"Finished Task {t.unique_id}")
    elif sys.argv[1] == "list":
        if len(sys.argv) == 3:
            t_2.list(sys.argv[2])
            # print("One")
        else:
            t_2.list()
            # print("Two")
    elif sys.argv[1] == "report":  
        t_2.report()      

main()