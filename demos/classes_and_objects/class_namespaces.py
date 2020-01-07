class MyClass:
    class_var = 1 #class namespace

    def __init__(self, i_var):
        self.i_var = i_var #instance namespace


x = 1 #global namespace

def print_stuff():
    x = 1 #local namespace
    print(x)



'''
Demonstrates the affects of
creating variables in the class namespace
vs. the instance namespace
'''
i1 = MyClass(1)
i2 = MyClass(2)

#instance namespace
print(i1.i_var)      #output: 1   
print(i2.i_var)      #output: 2

#class namespace
print(i1.class_var)  #output: 1
print(i2.class_var)  #output: 1

i1.class_var = 3
print(i1.class_var)  #output: 3
print(i2.class_var)  #output: 1

MyClass.class_var = 4
print(i1.class_var)  #output: 4
print(i2.class_var)  #output: 4

print(MyClass.i_var) #ILLEGAL!Cannot access instance attributes via class
