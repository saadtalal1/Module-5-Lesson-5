from abc import ABC
class animal(ABC):
    def move(self):
        print("I can move.")
class lion(animal):
    def move(self):
        print("I can sprint.")
class snake(animal):
    def move(self):
        print("I can slither.")
class sparrow(animal):
    def move(self):
        print("I can fly.")
class shark(animal):
    def move(self):
        print("I can swim.")
class kangaroo(animal):
    def move(self):
        print("I can jump.")
a=lion()
a.move()
b=snake()
b.move()
c=sparrow()
c.move()
d=shark()
d.move()
e=kangaroo()
e.move()


