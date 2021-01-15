import json

class Test:
    def __init__(self, name, age):
        self.name = name
        self.age=age
    
    def fromDic(self, dct):#json转成对象
        dic=json.loads(dct)
        return Test(dic['name'],int(dic['age']) )

class TestEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Test):
            return {'name':obj.name, 'age':obj.age}
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)


test = Test('aaa', 12)
jsonStr = json.dumps(test, cls=TestEncoder)#对象转json
print(type(jsonStr))
print(jsonStr)


newObj = test.fromDic(jsonStr)
newObj2=Test.fromDic(None,dct= jsonStr)
print(newObj.name)
print(newObj2.name)

 
 