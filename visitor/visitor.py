class Marine:
    def __init__(self):
        #your code here
        self.health = 100
        
    def accept(self,visitor):
        #your code here
        self.health -= visitor.visit_light()

class Marauder:
    def __init__(self):
        #your code here
        self.health = 125
        
    def accept(self,visitor):
        #your code here
        self.health -= visitor.visit_armored() 

class TankBullet:
    def visit_light(self,unit=21):
        #your code here
        return unit
        
    def visit_armored(self,unit=32):
        #your code here
        return unit