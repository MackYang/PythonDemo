# import sys

try:
    3/0
except Exception as ex:
    print(ex)

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:#具体异常类型可省略
#         print("Oops!  That was no valid number.  Try again...")
#         print("发生异常的类{0},具体的异常信息{1}".format(sys.exc_info()[0],sys.exc_info()[1]) )#输出异常信息
# def func():
#     raise IOError

# try:
#     func()
# except IOError as exc:
#     raise RuntimeError('异常链测试') from exc

# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except OSError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close()
# try:
#     raise Exception('spameggs')
# except:
#     print("Unexpected error:", sys.exc_info()[1])#输出异常信息
# # except Exception:# as inst:
# #     # print(type(inst))    # the exception instance
# #     # print(inst.args)     # arguments stored in .args
# #     # print(inst)          # __str__ allows args to be printed directly,
# #     #                      # but may be overridden in exception subclasses
# #     # x, y = inst.args     # unpack args
# #     # print('x =', x)
# #     # print('y =', y)
# #     print("Unexpected error:", sys.exc_info())#输出异常信息