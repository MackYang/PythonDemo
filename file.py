with open(r'D:\Learn\Python\Basis\test.txt','r+', encoding='UTF8') as f:
    #测试时要逐个注释来测
    #read_data = f.read()#一次性读取完所有内容
    #print(read_data)
    #oneLine=f.readline()
    #print(oneLine)  #只读一行,会从上次读取过的地方开始读
    # lines = f.readlines()#读余下的行,会从上次读取过的地方开始读
    # print(lines)  
    listData = list(f)#这个写法和readlines返回的都是list数组['这是第一行\n', '这是第2行\n', '再下边是空行\n', '\n']
    print(listData)
    # print(len(lines))
    # for line in f:
    #     print(line, end='')
    
    f.write("这是程序写入的")  #返回写入的内容长度
    f.seek(0)
    newContent = f.read()
    print(newContent)
