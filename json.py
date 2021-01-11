import json
data = json.dumps([1, 2, 3])
print(data)

class Test:
    def __init__(self, name, age):
        self.name = name
        self.age=age
    
test = Test('aaa', 12)
encoder=json.encoder.JSONEncoder()
objData = json.dump(test)
print(objData)
#json.dumps([1, 'simple', 'list'])