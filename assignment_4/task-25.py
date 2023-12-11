# task - Explain Inheritance in Python with an example? What is init? Or What
#        Is A Constructor In Python?

class person():

    def __init__(self,cno="93245900"):

        self.c = cno

class display(person):

    def __init__(self,c):

        print("hii")
        print(self.c)

obj = display()

print(obj)