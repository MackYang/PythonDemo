#需求:我想把arr中的数字分别放在setA,setB中,A和B中的数字在多线程执行完后也不能相同

import random
import threading

class A:
    setA = set()
    setB = set()
    arr = [1, 2, 3, 4, 5,6,7,8,9,0]
    threads = []
    
    def fun(self, condition):
        with condition:
            condition.wait()
            for i in self.arr:
                r = random.randrange(1, 100)
                if (r % 2 == 0):
                    self.setA.add(i)
                elif(not i in self.setA):
                    self.setB.add(i)
            condition.notify()
    
    def tFun(self):
        condition = threading.Condition()
        for i in range(10):
            t = threading.Thread(target=self.fun, args=(condition,))
            self.threads.append(t)
            t.start()
        for t in self.threads:
            t.join()
        print(self.setA)
        print(self.setB)

    
a = A()
a.tFun()


