import Queue

q = Queue.Queue()
q.put('ABC')
print q.qsize()

print q.get()
print q.qsize()
print q.empty()
print q.full()


stack = Queue.LifoQueue()
stack.put('ABC')
stack.put('DEF')

print stack.get()
print stack.get()








