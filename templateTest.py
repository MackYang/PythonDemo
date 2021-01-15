from string import Template#用于邮件内容等字符串模板
import sys
t = Template('${village}folk send $$10 to $cause.')
x = t.substitute(village='Nottingham', cause='the ditch fund')
print(x)

t = Template('Return the $item to $owner.')
    
try:
    d = dict(item='unladen swallow')
    x = t.substitute(d)#没提供的key会抛出异常
    print(x)
except:
    print(sys.exc_info()[1])

x = t.safe_substitute(d)#没提供的key就原样显示
print(x)
