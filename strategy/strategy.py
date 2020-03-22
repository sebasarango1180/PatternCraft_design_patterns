class Fly():
    def move(self,unit=10):
        #your code here
        return unit
        
class Walk():
    def move(self,unit=1):
        #your code here
        return unit

class Viking():
    def __init__(self):
        #your code here
        self.position = 0
        self.move_behavior = Walk()
  
    def move(self):
        #your code here
        self.position += self.move_behavior.move()