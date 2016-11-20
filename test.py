#!/usr/bin/python

from scheduler import *

def foo():
    ii = 0
    while ii < 10:
        print "foo" + str(ii)
        yield
        ii += 1

def bar():
    ii = 0
    while ii < 10:
        print "bar" + str(ii)
        yield
        ii += 1

if __name__ == "__main__":
    sched = Scheduler()
    sched.new(foo())
    sched.new(bar())
    sched.mainloop()
