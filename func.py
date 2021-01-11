# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)

# ask_ok('are you student?',reminder='222')

# def f(a, L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L

# print(f(1))
# print(f(2))
# print(f(3))

# def t(): 'this is comment,函数的注释与其同行'
#     pass
# print(t())#None

# def fib2(n):  'return Fibonacci series up to n' 
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)    # see below
#         a, b = b, a+b
#     return result


# f100 = fib2(100)  # call it
# print(f100)
 
# def varArgs(*ss):
#     for arg in ss:
#         print(arg)

# def dicArgs(**sss):
#     for arg in sss:
#         print(arg, ":", sss[arg])
    
# varArgs('111','222')
# dicArgs(b='abb', c='ccc')

# def make_incrementor(n):
#     return lambda x: x + n

# f = make_incrementor(42)
# print(f(0))

# print(f(1))

# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# for x in pairs:
#     print(x[0],'=',x[1])

def testFunc(age: int, name: str = "yh") -> int:
    '''
    函数的概要说明

    函数的详细说明xxxxx
    xxxxx
    '''
    return age-1

print(testFunc(18,"hhh"))
