import random
import threading
from threading import RLock
from threading import Lock

class A:
    setA = set()
    setB = set()
    arr = [1, 2, 3, 4, 5,6,7,8,9,0]
    threads = []
    lock=RLock()
    
    def fun(self, condition):
        
        with condition:
            condition.notify()
            condition.wait()
            for i in self.arr:
                r = random.randrange(1, 100)
                if (r % 2 == 0):
                    self.setA.add(i)
                elif(not i in self.setA):
                    self.setB.add(i)
            condition.notify()
    
    def fun2(self):
        self.lock.acquire()
        for i in self.arr:
            r = random.randrange(1, 10)
            if (r % 2 == 0):
                self.setA.add(i)
                if (i in self.setB):
                    self.setB.remove(i)
                    print(f'线程{threading.current_thread().name}移除{i}')
            elif(not i in self.setA):
                self.setB.add(i)
                print(f'线程{threading.current_thread().name}添加{i}')
        self.lock.release()

    
    def tFun(self):
        lock = Lock()
        condition = threading.Condition(lock)
        for i in range(10):
            
            t = threading.Thread(target=self.fun, args=(condition,))
            self.threads.append(t)
            t.start()
        for t in self.threads:
            t.join()
        print(self.setA)
        print(self.setB)

    def tFun2(self):
        for i in range(10):
            t = threading.Thread(target=self.fun2)
            self.threads.append(t)
            t.start()
        for t in self.threads:
            t.join()
        print(self.setA)
        print(self.setB)

a = A()
a.tFun2()


