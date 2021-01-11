import json
# data = json.dumps([1, 2, 3])
# print(data)

class Test:
    def __init__(self, name, age):
        self.name = name
        self.age=age
    
    def fromDic(self,dct):
        return Test(dct['name'], dct['age'])

class TestEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Test):
            return {'name':obj.name, 'age':obj.age}
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)


test = Test('aaa', 12)
encoder = TestEncoder()
t = json.dumps(test, cls=TestEncoder)
print(t)
# dic =TestEncoder.encode(test)
# print(dic)
# newObj = test.fromDic(dic)
# print(newObj)
#json.dumps([1, 'simple', 'list'])




 




# json.loads('{"__complex__": true, "real": 1, "imag": 2}',
#     object_hook=as_complex)

# list(ComplexEncoder().iterencode(2 + 1j))
