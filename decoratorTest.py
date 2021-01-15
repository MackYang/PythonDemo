#参照https://www.liaoxuefeng.com/wiki/1016959663602400/1017451662295584
#decorator用于AOP场景
#在不改变原有方法的情况下,增强原有方法的功能(在其前后执行某些代码)
#比如打印方法的执行时间等
import functools
import time

def execLog(func):
    '''不带参数的

    '''
    @functools.wraps(func)
    def warpper(*args, **kw):
        start = time.time()
        f = func(*args, **kw)
        end = time.time()
        print(f'{func.__name__}方法执行时长为{end- start} ms')
        return f
    return warpper



def execLogHasArgs(text):
    '''带参数的
    
    '''
    def decorater(func):
        @functools.wraps(func)
        def warpper(*args, **kw):
            start = time.time()
            f = func(*args, **kw)
            end = time.time()
            print(f'{func.__name__}方法执行时长为{end- start} ms,传入的参数为{text}')
            return f
        return warpper
    return decorater

@execLog
def someFuncA():
    time.sleep(1)
    print('这是方法A')


@execLogHasArgs('aaa')
def someFuncB():
    time.sleep(1)
    print('这是方法B')

someFuncA()
someFuncB()
