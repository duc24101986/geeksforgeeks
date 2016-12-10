import threading

def printSomething(str):
    count = 0
    while(count < 10):
        print str
        count +=1
    
t1 = threading.Thread(target=printSomething, args= ("Thread 1",))
t2 = threading.Thread(target=printSomething, args= ("Thread 2",))
t1.start()
t2.start()

t1.join()
t2.join()



