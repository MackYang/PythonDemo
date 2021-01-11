x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

words = ['cat', 'window', 'end', 'defenestrate']
for w in words:
    if w == 'cat':
        continue
    elif w == 'end':
        break
    else:
        print(w, len(w))

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        else:
            loop fell through without finding a factor
            print(n, 'is a prime number')
