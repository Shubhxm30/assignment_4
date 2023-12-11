# task - Write a Python class named Circle constructed by a radius and two
#        methods which will compute the area and the perimeter of a circle

class circle():
    def __init__(self,radius):
        
        self.r = radius

    def area (self):

        return self.r**2*3.14
    
    def perimiter (self):

        return 2* self.r * 3.14
    
new = circle(21)

print(new.area())
print(new.perimiter())