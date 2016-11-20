class Task(object):
    task_id = 0
    def __init__(self, target):
        Task.task_id = Task.task_id + 1
        self.tid = Task.task_id
        self.name = target.__name__
        self.target = target
        self.sendval = None
    def run(self):
        return self.target.send(self.sendval)

