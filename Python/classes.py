import numpy

class MyClass(object):
    common= 10
    
    def __init__(self):
        self.myvariable= 3

    def myfunction(self, arg):
        self.myvariable= arg
        return self.myvariable


#instanciation of the class
instance1= MyClass()

#changing variables of the class
print (instance1.myfunction(1) )

# Binding an object to the old variable one
instance2= MyClass()

MyClass.common= 30
print (MyClass.common, instance1.common)

instance2.common= 10
print (MyClass.common, instance1.common, instance2.common)

instance1.common = 50
print (MyClass.common, instance1.common, instance2.common)

MyClass.common=100
print (MyClass.common, instance1.common, instance2.common)


# This is inheritance or what I call WRAPPER

class OtherClass(MyClass):  # -> OtherClass inherits everything from MyClass
    
    def __init__(self, arg):
        self.othervariable= arg

    def myotherfunction(self):
        return self.othervariable
        

instance3= OtherClass(3)
print (instance3.myfunction(2), instance3.myotherfunction())
