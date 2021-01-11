class Parent():
    globalName = 'this is globalName'
    def __init__(self, parentName :str):
        self.parentName = parentName
        
class Son(Parent):
    def __init__(self, sonName):
        self.sonName = self.globalName + sonName
        
print(Son.globalName)

s = Son("son_xx")
print(s.sonName)

p=Parent('parent_yyy')
print(Parent.globalName)
print(p.parentName)

#检查一个实例的类型是否是某类或其派生类
print(isinstance(s, Parent))
print(isinstance(s, Son))
#检查某类是否是某类的子类
print(issubclass(Son, Parent))
print(issubclass(Parent, Son))

