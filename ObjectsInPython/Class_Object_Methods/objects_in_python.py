

# Create your first empty class

class MyFirstClass:
    pass

#create object

obj = MyFirstClass()
print(obj)
#output : <__main__.MyFirstClass object at 0x102923c40>

#Now this do not have any attribute
#Just add two coordinates attribute

obj.x = 10
obj.y = 20

print(obj.x, obj.y)


class MySecondClass:
    def reset(self):
        self.x = 0
        self.y = 0


obj = MySecondClass()
obj.x = 10
obj.y = 20
print(obj.x, obj.y)
obj.reset()
print(obj.x, obj.y)

# Another way to call methode in class object
# However, the method really is just a function that happens to be on a class. Instead
# of calling the method on the object, we can invoke the function on the class, explicitly
# passing our object as the self argument:
MySecondClass.reset(obj)
obj.reset()
