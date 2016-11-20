import task
from Queue import *

class Scheduler(object):
    def __init__(self):
        self.ready = Queue()
        self.taskmap = {}
    def exit(self, t):
        print "Task", t.name, "with id", t.tid, "exited"
        del self.taskmap[t.tid]
    def schedule(self, task):
        self.ready.put(task)
    def new (self, target):
        t = task.Task(target)
        self.taskmap[t.tid] = t
        self.schedule(t)
        return t.tid
    def mainloop(self):
        while self.taskmap:
            t = self.ready.get()
            try:
                t.run()
            except StopIteration:
                self.exit(t)
                continue
            self.schedule(t)


