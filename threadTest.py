import threading
import time

class T:
    num = 0

    lock = threading.RLock()


    # 调用acquire([timeout])时，线程将一直阻塞，
    # 直到获得锁定或者直到timeout秒后（timeout参数可选）。
    # 返回是否获得锁。
    def Func(self ):
        self.lock.acquire()
        
        self.num += 1
        time.sleep(1)
        print(self.num)
        self.lock.release()


    def Test(self):
        for i in range(10):
            t = threading.Thread(target=self.Func)
            t.start()

t = T()
t.Test()