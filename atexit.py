
from atexit import register

try:
    with open("counterfile") as infile:
        _count = int(infile.read())
        print(_count)
except FileNotFoundError:
    _count = 0

def incrcounter(n):
    global _count
    _count = _count + n

@register
def savecounter():
    print('called')
    incrcounter(1)
    with open("counterfile", "w") as outfile:
        outfile.write("%d" % _count)

