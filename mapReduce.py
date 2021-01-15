#https://www.liaoxuefeng.com/wiki/1016959663602400/1017329367486080
#map 有点和js中数组的map类似,
#map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list
a = "12345"
b = list(map(int, a))
c = map(int, a)
print(b)#[1, 2, 3, 4, 5]
print(type(c))  #<class 'map'>

#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce

def add(a, b):
    return a + b

listA = [1, 2, 3, 4, 5]
result = reduce(add, listA)
print(result)#15