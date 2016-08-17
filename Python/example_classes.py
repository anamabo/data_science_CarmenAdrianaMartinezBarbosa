
class MyClass(object):
    common= 10
    
    def __init__(self):
        self.myvariable= 3

    def myfunction(self, arg):
        self.myvariable= arg
        return self.myvariable


#instanciation of the class
instance1= MyClass()

instance2= MyClass()

# In the following lines I'm changing the value of common three times.
# Which is the real value of common then?
MyClass.common= 30
instance2.common= 10
instance1.common = 50
print (MyClass.common, instance1.common, instance2.common)

# In this case Which is the real value of common?
# In which cases we bind an instance with an old value of a varible?
MyClass.common=100
print (MyClass.common, instance1.common, instance2.common)

# Thanks for your anwer Nischal!
