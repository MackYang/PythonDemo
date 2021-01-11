cubes = [1, 8, 27, 65, 125]
changed = sorted(cubes,reverse=True)
print(changed)

4 ** 3  # the cube of 4 is 64, not 65!
print(cubes)
cubes[3] = 64  # replace the wrong value
print(cubes)
cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
print(cubes)
cubes=[]
print(cubes)
print(len(cubes))

#给切片赋值也是可以的，这样甚至可以改变列表大小，或者把列表整个清空:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

# replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)

# now remove them
letters[2:5] = []
print(letters)

#也可以嵌套列表 (创建包含其他列表的列表), 比如说:

 
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)#[['a', 'b', 'c'], [1, 2, 3]]

print(x[0])#['a', 'b', 'c']

print(x[0][1])#b

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b