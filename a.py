a="你好p,ython"
b = "hello"
print(b[-2])  # from right start
#[x:y] from x to y-1
print(b[0:2])  # he
print(b[1:3])# el
print(b[2:5])  # llo
print(b[2:])  # llo
print(b[5:])  # space
print(b[:4])# hell

d=a+b
print(a + b)
#这是注释
e = 3*b+a#replace 3 times b
print(e)
mutliLine = ('aaa'
'\nbbb'
'\nccc')

mutliLineB = '''firstLine
SecondLine
'''
print(mutliLine)
print(mutliLineB)

print(str.split(a,','))
print(str.upper(a))
print(str.replace(a,'y','K'))
 
k='this is placeholder'
from string import Template
t=Template('test:${content}')
print(t.substitute(content=k))

m = 'test2:{0},{1}'.format(k, a)
print(m)