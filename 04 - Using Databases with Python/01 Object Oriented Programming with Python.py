# Dallin Romney
# Object Oriented Programming Notes

class Inheritor:
    
    x = 2;
    
    def printMessage(self):
        print('message', self.x)
        
class ObjectName(Inheritor):
    
    def __init__ (self, a, b):
        self.x += a*b
        
    def printMessage2(self):
        print('New Value:', self.x)

newObject = ObjectName(2, 3)
newObject.printMessage2()
